from data_strucutre.LinkedList import Node


def remove_dups(linked_list):
    """
    Remove duplicates of a linked list
    """
    cur = linked_list
    if not cur:
        return None
    visited = set()
    visited.add(cur.data)
    while cur and cur.nextNode:
        if cur.nextNode.data in visited:
            cur.nextNode = cur.nextNode.nextNode
        else:
            visited.add(cur.nextNode.data)
            cur = cur.nextNode
    return linked_list


def return_kith_to_last(linked_list, k):
    """
    Return a linked list with elements from kith item to last
    """
    i = 1
    cur = linked_list
    while cur:
        if i == k:
            return cur
        cur = cur.nextNode
        i += 1
    return None


def delete_middle_node(linked_list):
    """
    Remove the middle node of a linked list
    """
    # use the runner technique, when fast reaches the end, slow is in the middle
    slow_prev = None
    slow_cur = linked_list
    fast_cur = linked_list
    while fast_cur.nextNode and fast_cur.nextNode.nextNode:
        fast_cur = fast_cur.nextNode.nextNode
        slow_prev = slow_cur
        slow_cur = slow_cur.nextNode

    if not slow_prev:
        return fast_cur.nextNode
    elif slow_prev.nextNode:
        slow_prev.nextNode = slow_prev.nextNode.nextNode
    return linked_list


def partition(linked_list, partition):
    """
    Partition the linked list such that all nodes with value less than partition are in front of the nodes
    with value greater than or equal to partition, inclusive.
    """
    less_than_partition = Node("Dummy")
    greater_than_partition = Node("Dummy")
    less_than_head = less_than_partition
    greater_than_head = greater_than_partition
    cur = linked_list
    while cur:
        if cur.data < partition:
            less_than_partition.nextNode = cur
            less_than_partition = less_than_partition.nextNode
        else:
            greater_than_partition.nextNode = cur
            greater_than_partition = greater_than_partition.nextNode
        prev = cur
        cur = cur.nextNode
        prev.nextNode = None

    if less_than_head.nextNode:
        less_than_partition.nextNode = greater_than_head.nextNode
        return less_than_head.nextNode
    else:
        return greater_than_head.nextNode


def sum_lists(linked_list_1, linked_list_2):
    """
    Given 2 linked lists, return the sum of 2 numbers. The 2 numbers are extracted from the 2 linked lists such that
    all values of the linked list represent a revered digit of the number.
    i.e if input is
    linked_list_1: 1 -> 2 -> 3
    linked_list_2: 4 -> 5 -> 6
    then output is: 321 + 654 = 975
    """

    def getAssociatedNum(linked_list):
        cur = linked_list
        i = 0
        aggregate = 0
        while cur:
            aggregate += cur.data * (10 ** i)
            cur = cur.nextNode
            i += 1
        return aggregate

    return getAssociatedNum(linked_list_1) + getAssociatedNum(linked_list_2)


def palindrome(linked_list):
    """
    Determine whether or not the linked list is a palindrome.
    """
    visited_half = []

    # use the runner technique
    slow_cur = linked_list
    fast_cur = linked_list
    while fast_cur and fast_cur.nextNode:
        visited_half.append(slow_cur)
        fast_cur = fast_cur.nextNode.nextNode
        slow_cur = slow_cur.nextNode

    # if there's only one node, and not 2 nodes
    if not slow_cur.nextNode and not linked_list.nextNode == slow_cur:
        return True
    # odd num of elements,  then we skip one
    elif fast_cur and not fast_cur.nextNode:
        slow_cur = slow_cur.nextNode

    # reverse traverse/stack
    for i in range(len(visited_half) - 1, -1, -1):
        if visited_half[i].data != slow_cur.data:
            return False
        slow_cur = slow_cur.nextNode

    return True


def intersection(linked_list_1, linked_list_2):
    """
    Given 2 linked lists, determine whether or not those two linked lists merge into one.
    i.e.
    input:
    0 -> 1 -> 2 -> 3
                      -> 7 -> 8 -> 9
         4 -> 5 -> 6

    output: 7 -> 8 -> 9
    """

    def get_count_and_last(linked_list):
        n = 0
        cur = linked_list
        while cur.nextNode:
            cur = cur.nextNode
            n += 1
        return [n, cur]

    [n1, linked_list_1_last] = get_count_and_last(linked_list_1)
    [n2, linked_list_2_last] = get_count_and_last(linked_list_2)

    linked_list_1_cur = linked_list_1
    linked_list_2_cur = linked_list_2

    if n2 > n1:
        diff = n2 - n1
        offset = linked_list_2_cur
    else:
        diff = n1 - n2
        offset = linked_list_1_cur

    # if they don't intersect
    if linked_list_1_last != linked_list_2_last:
        return None

    for i in range(diff):
        offset = offset.nextNode

    other = linked_list_1_cur if offset == linked_list_2_cur else linked_list_2_cur
    while offset:
        if offset == other:
            return offset
        else:
            offset = offset.nextNode
            other = other.nextNode


def loop_detection_set(linked_list):
    """
    Check whether or not there's a loop in the linked list, if there is, return the head.
    """
    visited = set()
    cur = linked_list
    while cur:
        if cur in visited:
            return cur
        else:
            visited.add(cur)
        cur = cur.nextNode


def loop_detection_runner_technique(linked_list):
    """
    Check whether or not there's a loop in the linked list, if there is, return the head.
    """
    # let node 2 run twice as fast as node 1
    # after k iterations, node 1 at the start of loop
    # let L denote loop size
    # node 2 at position 2k => (2k - k) % L <=> k % L pos into the loop
    # when node 1 at start of the loop, node 2 at k % L into the loop
    # in every iteration, node 2 catches up to node 1 node closer
    # node 1 and node 2 is eventually meet at (L - k) % L,
    # since node 1 starts at pos 0 of loop, they are (L - k) % L apart
    # keep node 2 at pos, reset node 1 at start of linked list,
    # let both run one step at a time, in k iterations, node 1 at start of loop
    # node 2 at (L - k) % L, run k more times in loop
    # => (L - k) % L + k % L <=> pos 0 of loop/start of loop
    # they meet at the start of the loop, return the start of the loop

    slow_cur = linked_list
    fast_cur = linked_list

    while fast_cur and fast_cur.nextNode:
        fast_cur = fast_cur.nextNode.nextNode
        slow_cur = slow_cur.nextNode
        if id(fast_cur) == id(slow_cur):
            break

    if not fast_cur or not fast_cur.nextNode:
        return None

    slow_cur = linked_list

    while id(slow_cur) != id(fast_cur):
        slow_cur = slow_cur.nextNode
        fast_cur = fast_cur.nextNode

    return fast_cur
