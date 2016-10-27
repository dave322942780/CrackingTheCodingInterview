class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    @staticmethod
    def create_linked_list(lst):
        head = cur = None
        for i in lst:
            node = Node(i)
            if head is None:
                head = cur = node
            else:
                cur.nextNode = node
                cur = node
        return head

    def __eq__(self, other):
        if other is None or type(other) != Node:
            return False
        self_cur = self
        other_cur = other
        while self_cur and other_cur:
            if self_cur.data != other_cur.data:
                return False
            else:
                self_cur = self_cur.nextNode
                other_cur = other_cur.nextNode
        if self_cur and not other_cur or other_cur and not self_cur:
            return False
        return True

    def __repr__(self):
        res = []
        cur = self
        while cur:
            res.append(str(cur.data))
            cur = cur.nextNode
        return "<" + ",".join(res) + ">"

