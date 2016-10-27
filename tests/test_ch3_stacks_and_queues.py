import unittest

import time

from ch3_stacks_and_queues import MultiStacks, MinQueue, StackOfStacks, TwoStackQueue, Stack, sort_stack, AnimalShelterIterative, \
    Dog, Cat, AnimalShelterTimeStamp


class StacksAndQueuesTestCase(unittest.TestCase):
    def test_multi_stacks(self):

        # test multi stacks
        multi_stack = MultiStacks(5, 3)

        # test dynamic push into 1 stack
        multi_stack.push(1, 1)
        multi_stack.push(1, 2)
        multi_stack.push(1, 3)
        multi_stack.push(1, 4)
        multi_stack.push(1, 5)
        self.assertEqual(multi_stack.pop(1), 5)
        self.assertEqual(multi_stack.pop(1), 4)
        self.assertEqual(multi_stack.pop(1), 3)
        self.assertEqual(multi_stack.pop(1), 2)
        self.assertEqual(multi_stack.pop(1), 1)

        # test push into multiple stacks
        multi_stack.push(0, 1)
        multi_stack.push(0, 2)
        multi_stack.push(1, 3)
        multi_stack.push(1, 4)
        multi_stack.push(2, 5)
        self.assertEqual(multi_stack.pop(0), 2)
        self.assertEqual(multi_stack.pop(0), 1)
        self.assertEqual(multi_stack.pop(1), 4)
        self.assertEqual(multi_stack.pop(1), 3)
        self.assertEqual(multi_stack.pop(2), 5)

        # test dynamic sizing
        multi_stack = MultiStacks(3, 2)
        multi_stack.push(1, 1)
        multi_stack.push(1, 2)
        multi_stack.push(1, 3)
        self.assertEqual(multi_stack.pop(1), 3)
        multi_stack.push(0, 1)
        self.assertEqual(multi_stack.pop(1), 2)
        multi_stack.push(0, 2)
        self.assertEqual(multi_stack.pop(1), 1)
        multi_stack.push(0, 3)
        self.assertEqual(multi_stack.pop(0), 3)
        self.assertEqual(multi_stack.pop(0), 2)
        self.assertEqual(multi_stack.pop(0), 1)

        # test push onto full stacks and pop on empty stack
        multi_stack = MultiStacks(3, 2)
        multi_stack.push(1, 1)
        multi_stack.push(0, 3)
        multi_stack.push(1, 2)
        try:
            multi_stack.push(0, 4)
            self.fail("no exception raised when push onto full stacks")
        except Exception as e:
            pass
        self.assertEqual(multi_stack.pop(1), 2)
        self.assertEqual(multi_stack.pop(1), 1)
        try:
            multi_stack.pop(1)
            self.fail("no exception raised when pop from empty")
        except Exception as e:
            pass

    def test_min_queue(self):

        # test general
        min_queue = MinQueue()
        min_queue.push(5)
        self.assertEqual(5, min_queue.min())
        min_queue.push(2)
        self.assertEqual(2, min_queue.min())
        min_queue.push(3)
        self.assertEqual(2, min_queue.min())
        self.assertEqual(min_queue.pop(), 3)
        self.assertEqual(2, min_queue.min())
        self.assertEqual(min_queue.pop(), 2)
        self.assertEqual(5, min_queue.min())
        self.assertEqual(min_queue.pop(), 5)

        # test pop from empty
        try:
            min_queue.pop()
            self.fail("no exception raised when pop form empty")
        except Exception as e:
            pass

    def test_stack_of_plates(self):

        # test push and pop
        min_queue = StackOfStacks(3)
        min_queue.push(1)
        min_queue.push(2)
        min_queue.push(3)
        min_queue.push(4)
        min_queue.push(5)
        self.assertEqual(5, min_queue.pop())
        self.assertEqual(4, min_queue.pop())
        self.assertEqual(3, min_queue.pop())
        self.assertEqual(2, min_queue.pop())
        self.assertEqual(1, min_queue.pop())
        try:
            min_queue.pop()
            self.fail("no exception raised when pop form empty")
        except Exception as e:
            pass

        # test popAt, pop
        min_queue = StackOfStacks(3)
        min_queue.push(1)
        min_queue.push(2)
        min_queue.push(3)
        min_queue.push(4)
        min_queue.push(5)
        min_queue.push(6)
        min_queue.push(7)
        min_queue.push(8)
        min_queue.push(9)
        min_queue.push(10)
        self.assertEqual(6, min_queue.popAt(1))
        self.assertEqual(3, min_queue.popAt(0))
        self.assertEqual(5, min_queue.popAt(1))
        self.assertEqual(4, min_queue.popAt(1))
        self.assertEqual(9, min_queue.popAt(1))
        self.assertEqual(10, min_queue.pop())
        self.assertEqual(8, min_queue.pop())
        self.assertEqual(7, min_queue.pop())
        self.assertEqual(2, min_queue.pop())
        self.assertEqual(1, min_queue.pop())
        try:
            min_queue.pop()
            self.fail("no exception raised when pop form empty")
        except Exception as e:
            pass

    def test_two_stack_queue(self):
        # test queue
        two_stack_queue = TwoStackQueue()
        two_stack_queue.push(1)
        two_stack_queue.push(2)
        two_stack_queue.push(3)
        two_stack_queue.push(4)
        two_stack_queue.push(5)
        two_stack_queue.push(6)
        two_stack_queue.push(7)
        self.assertEqual(1, two_stack_queue.pop())
        self.assertEqual(2, two_stack_queue.pop())
        self.assertEqual(3, two_stack_queue.pop())
        self.assertEqual(4, two_stack_queue.pop())
        self.assertEqual(5, two_stack_queue.pop())
        self.assertEqual(6, two_stack_queue.pop())
        self.assertEqual(7, two_stack_queue.pop())
        try:
            two_stack_queue.pop()
            self.fail("no exception raised when pop form empty")
        except Exception as e:
            pass

    def test_sort_stack(self):

        # test empty
        stack = Stack()
        sort_stack(stack)

        # test duplicate/general
        stack = Stack()
        stack.push(3)
        stack.push(5)
        stack.push(4)
        stack.push(4)
        stack.push(1)
        sort_stack(stack)
        self.assertEqual(1, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(5, stack.pop())

    def test_animal_shelter(self):
        animal_shelter = AnimalShelterIterative()
        animal_shelter.enqueue(Cat("cat 1"))
        animal_shelter.enqueue(Cat("cat 2"))
        animal_shelter.enqueue(Dog("dog 1"))
        animal_shelter.enqueue(Dog("dog 2"))
        animal_shelter.enqueue(Cat("cat 3"))
        self.assertEqual(animal_shelter.dequeue(), Cat("cat 1"))
        self.assertEqual(animal_shelter.dequeue_dog(), Dog("dog 1"))
        self.assertEqual(animal_shelter.dequeue_cat(), Cat("cat 2"))
        self.assertEqual(animal_shelter.dequeue(), Dog("dog 2"))
        self.assertEqual(animal_shelter.dequeue(), Cat("cat 3"))

        # python can not differentiate timestamps of commands that execute too closely together, time-wise
        animal_shelter = AnimalShelterTimeStamp()
        animal_shelter.enqueue(Cat("cat 1"))
        time.sleep(0.001)
        animal_shelter.enqueue(Cat("cat 2"))
        time.sleep(0.001)
        animal_shelter.enqueue(Dog("dog 1"))
        time.sleep(0.001)
        animal_shelter.enqueue(Dog("dog 2"))
        time.sleep(0.001)
        animal_shelter.enqueue(Cat("cat 3"))
        self.assertEqual(animal_shelter.dequeue(), Cat("cat 1"))
        self.assertEqual(animal_shelter.dequeue_dog(), Dog("dog 1"))
        self.assertEqual(animal_shelter.dequeue_cat(), Cat("cat 2"))
        self.assertEqual(animal_shelter.dequeue(), Dog("dog 2"))
        self.assertEqual(animal_shelter.dequeue(), Cat("cat 3"))