class Queue(object):
    class Node(object):
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self, lst=[]):
        self.head = None
        self.tail = None
        for i in lst:
            self.enqueue(i)

    def enqueue(self, item):
        node = self.Node(item)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = self.tail.next_node

    def dequeue(self):
        if not self.head:
            raise IndexError("Queue is empty")
        tmp = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next_node
        return tmp

    def is_empty(self):
        return not bool(self.head)

    def peek(self):
        if not self.head:
            raise IndexError("Queue is empty")
        return self.head.data

    def __repr__(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next_node
        return str(res)
