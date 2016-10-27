import datetime

from data_strucutre.Queue import Queue


class MultiStacks(object):
    class StackTracker(object):
        def __init__(self, start, cur_offset, size):
            self.start = start
            self.cur_offset = cur_offset
            self.size = size

        def __repr__(self):
            return str([self.start, self.cur_offset, self.size])

    def __init__(self, fixed_size, num_of_stacks):
        def allocate_initial_heads():
            i = 0
            distributed_remainder = fixed_size % num_of_stacks
            distributed_size = fixed_size / num_of_stacks
            res = []
            while i < fixed_size:
                stack_size = distributed_size
                if distributed_remainder:
                    distributed_remainder -= 1
                    stack_size += 1
                res.append(self.StackTracker(i, -1, stack_size))
                i += stack_size
            assert len(res) == num_of_stacks
            return res

        self.num_of_stacks = num_of_stacks
        self.stacks = [None] * fixed_size  # use of fixed length to mimic array in Java
        self.stack_trackers = allocate_initial_heads()

    def push(self, idx, value):
        assert idx < self.num_of_stacks

        def push_and_reallocate_stack_sizes():
            free_space = -1
            for j in self.stack_trackers:
                free_space += j.size - j.cur_offset - 1
            if free_space < 0:
                raise OverflowError("Stacks are all full")

            distributed_remainder = free_space % self.num_of_stacks
            distributed_size = free_space / self.num_of_stacks
            reallocated_stacks = [None] * len(self.stacks)  # use of fixed length to mimic array in Java

            for i, stack_tracker in enumerate(self.stack_trackers):
                start_idx = self.stack_trackers[i - 1].start + self.stack_trackers[i - 1].size if i > 0 else 0
                for j in range(stack_tracker.cur_offset + 1):
                    reallocated_stacks[start_idx + j] = self.stacks[stack_tracker.start + j]
                stack_tracker.start = start_idx
                stack_tracker.size = stack_tracker.cur_offset + 1 + distributed_size
                if self.stack_trackers[idx] == stack_tracker:
                    stack_tracker.size += 1
                if distributed_remainder:
                    distributed_remainder -= 1
                    stack_tracker.size += 1
            self.stacks = reallocated_stacks
            self.push(idx, value)

        target_stack = self.stack_trackers[idx]
        if target_stack.cur_offset < target_stack.size - 1:
            target_stack.cur_offset += 1
            self.stacks[target_stack.start + target_stack.cur_offset] = value
        else:
            push_and_reallocate_stack_sizes()

    def pop(self, idx):
        target_stack = self.stack_trackers[idx]
        if target_stack.cur_offset != -1:
            idx_to_remove = target_stack.start + target_stack.cur_offset
            item = self.stacks[idx_to_remove]
            self.stacks[idx_to_remove] = None
            target_stack.cur_offset -= 1
            return item


class MinQueue(object):
    queue = []
    min_queue = []

    def push(self, item):
        self.queue.append(item)
        if not self.min_queue:
            self.min_queue.append(item)
        elif self.min_queue[-1] >= item:
            self.min_queue.append(item)

    def pop(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        item = self.queue.pop()
        if item == self.min_queue[-1]:
            min = self.min_queue.pop()
        return item

    def min(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        else:
            return self.min_queue[-1]


class StackOfStacks(object):
    def __init__(self, threshold):
        self.stacks = []
        self.threshold = threshold

    def push(self, item):
        if not self.stacks or self.stacks and len(self.stacks[-1]) == self.threshold:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        if self.stacks:
            item = self.stacks[-1].pop()
            if not self.stacks[-1]:
                self.stacks.pop()
            return item
        else:
            raise IndexError("Queue is empty")

    def popAt(self, idx):

        if len(self.stacks) > idx:
            item = self.stacks[idx].pop()
            if not self.stacks[idx]:
                self.stacks.pop(idx)
            return item
        else:
            raise IndexError("Queue is empty")


class TwoStackQueue(object):
    def __init__(self, limit=5):
        self.inbox = []
        self.outbox = []
        self.limit = limit

    def _refill_outbox(self):
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def push(self, item):
        self.inbox.append(item)
        if len(self.inbox) > self.limit:
            self._refill_outbox()

    def pop(self):
        if not self.outbox:
            self._refill_outbox()
        if not self.outbox:
            raise IndexError("Queue is empty")
        else:
            return self.outbox.pop()


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def sort_stack(stack):
    # special case, when stack is empty
    if stack.is_empty():
        return

    i = 0
    queue_size = 0
    while i == 0 or i < queue_size:

        # top i items are already sorted, ignore them
        tmp_stack = Stack()
        for j in range(i):
            tmp_stack.push(stack.pop())

        # get the largest from ith to last (a.k.a ith largest, since 0 - i are already sorted)
        largest = None
        idx_of_largest = None
        idx = 0
        while not stack.is_empty():
            if i == 0:
                queue_size += 1
            item = stack.pop()
            if largest is None or item > largest:
                largest = item
                idx_of_largest = idx
            tmp_stack.push(item)
            idx += 1

        # since we're using a stack, so idx is in revers order => size - counted idx
        idx = idx - idx_of_largest - 1
        reserved_largest = None
        while not tmp_stack.is_empty():
            item = tmp_stack.pop()
            if idx == 0:
                reserved_largest = item
            else:
                stack.push(item)
            idx -= 1
        stack.push(reserved_largest)
        i += 1


class Animal(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not other:
            return False
        elif type(self) != type(other):
            return False
        elif self.name != other.name:
            return False
        return True


class Cat(Animal):
    pass


class Dog(Animal):
    pass



class AnimalShelterIterative(object):
    class ExtendedQueue(Queue):
        def dequeue(self, data_type=None):
            if not data_type:
                return Queue.dequeue(self)
            else:
                cur = self.head
                # if item is 1st in list
                if cur and type(cur.data) == data_type:
                    self.head = self.head.next_node
                    # if there's only one node in the list
                    if not self.head:
                        self.tail = None
                    return cur

                while cur and cur.next_node:
                    if type(cur.next_node.data) == data_type:
                        tmp = cur.next_node
                        cur.next_node = cur.next_node.next_node
                        if not cur.next_node:
                            self.tail = cur
                        return tmp
                    cur = cur.next_node
                raise IndexError("Queue is empty")

    def __init__(self):
        self.cat_queue = self.ExtendedQueue()
        self.dog_queue = self.ExtendedQueue()
        self.cat_dog_queue = self.ExtendedQueue()

    def enqueue(self, cat_or_dog):
        if type(cat_or_dog) == Cat:
            self.cat_queue.enqueue(cat_or_dog)
        elif type(cat_or_dog) == Dog:
            self.dog_queue.enqueue(cat_or_dog)
        else:
            raise TypeError("Neither a dog nor a cat")
        self.cat_dog_queue.enqueue(cat_or_dog)

    def dequeue_dog(self):
        self.cat_dog_queue.dequeue(Dog)
        return self.dog_queue.dequeue()

    def dequeue_cat(self):
        self.cat_dog_queue.dequeue(Cat)
        return self.cat_queue.dequeue()

    def dequeue(self):
        cat_or_dog = self.cat_dog_queue.peek()

        if not self.dog_queue.is_empty() and cat_or_dog == self.dog_queue.peek():
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

class AnimalShelterTimeStamp(object):
    class ExtendedQueue(Queue):
        class TimeStampedItem:
            def __init__(self, item):
                self.item = item
                self.time_stamp = datetime.datetime.now()


    def __init__(self):
        self.cat_queue = self.ExtendedQueue()
        self.dog_queue = self.ExtendedQueue()
        self.cat_dog_queue = self.ExtendedQueue()

    def enqueue(self, cat_or_dog):
        if type(cat_or_dog) == Cat:
            self.cat_queue.enqueue(self.ExtendedQueue.TimeStampedItem(cat_or_dog))
        elif type(cat_or_dog) == Dog:
            self.dog_queue.enqueue(self.ExtendedQueue.TimeStampedItem(cat_or_dog))

    def dequeue_dog(self):
        return self.dog_queue.dequeue().item

    def dequeue_cat(self):
        return self.cat_queue.dequeue().item

    def dequeue(self):
        if self.cat_queue.is_empty() and self.dog_queue.is_empty():
            raise IndexError("Queue is empty")
        elif self.dog_queue.is_empty():
            return self.cat_queue.dequeue().item
        elif self.cat_queue.is_empty():
            return self.dog_queue.dequeue().item
        else:
            next_dog = self.dog_queue.peek()
            next_cat = self.cat_queue.peek()
            if next_cat.time_stamp < next_dog.time_stamp:
                return self.cat_queue.dequeue().item
            else:
                return self.dog_queue.dequeue().item