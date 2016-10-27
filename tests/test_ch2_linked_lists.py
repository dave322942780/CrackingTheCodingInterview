import unittest

from ch2_linked_lists import remove_dups, return_kith_to_last, delete_middle_node, partition, sum_lists, palindrome, \
    intersection, loop_detection_set, loop_detection_runner_technique
from data_strucutre.LinkedList import Node


class StringMethodsTestCase(unittest.TestCase):
    def test_remove_dups(self):
        # test beginning and single duplicate
        input_linked_list = [1, 1]
        input_head = Node.create_linked_list(input_linked_list)
        input_head = remove_dups(input_head)
        self.assertEqual(input_head, Node.create_linked_list([1]))

        # test beginning duplicates, multiple duplicates
        input_linked_list = [1, 1, 2, 2]
        input_head = Node.create_linked_list(input_linked_list)
        input_head = remove_dups(input_head)
        self.assertEqual(input_head, Node.create_linked_list([1, 2]))

        # test duplicates scattered all over the list
        linked_list = [1, 2, 3, 5, 6, 5, 4, 8, 7, 6, 4, 1, 2, 3]
        input_head = Node.create_linked_list(linked_list)
        input_head = remove_dups(input_head)
        self.assertEqual(input_head, Node.create_linked_list([1, 2, 3, 5, 6, 4, 8, 7]))

    def test_return_kith_to_last(self):
        # general test
        linked_list = [5, 4, 3, 2, 1]
        input_head = Node.create_linked_list(linked_list)
        input_head = return_kith_to_last(input_head, 3)
        self.assertEqual(input_head, Node.create_linked_list([3, 2, 1]))

    def test_delete_middle_node(self):
        # test 2 elements
        linked_list = [1, 2]
        input_head = Node.create_linked_list(linked_list)
        input_head = delete_middle_node(input_head)
        self.assertEqual(input_head, Node.create_linked_list([2]))

        # test even num of elements
        linked_list = [1, 2, 3, 4, 5, 6]
        input_head = Node.create_linked_list(linked_list)
        input_head = delete_middle_node(input_head)
        self.assertEqual(input_head, Node.create_linked_list([1, 2, 4, 5, 6]))

        # test odd num of elements
        linked_list = [1, 2, 3]
        input_head = Node.create_linked_list(linked_list)
        input_head = delete_middle_node(input_head)
        self.assertEqual(input_head, Node.create_linked_list([1, 3]))

    def test_partition(self):
        # test only less than
        linked_list = [1, 2, 3]
        input_head = Node.create_linked_list(linked_list)
        input_head = partition(input_head, 4)
        self.assertEqual(input_head, Node.create_linked_list([1, 2, 3]))

        # test only greater than
        linked_list = [4, 5, 6, 7]
        input_head = Node.create_linked_list(linked_list)
        input_head = partition(input_head, 4)
        self.assertEqual(input_head, Node.create_linked_list([4, 5, 6, 7]))

        # test only less than
        linked_list = [3, 2, 1]
        input_head = Node.create_linked_list(linked_list)
        input_head = partition(input_head, 4)
        self.assertEqual(input_head, Node.create_linked_list([3, 2, 1]))

        # test general
        linked_list = [1, 2, 6, 4, 3, 5, 6, 2]
        input_head = Node.create_linked_list(linked_list)
        input_head = partition(input_head, 4)
        self.assertEqual(input_head, Node.create_linked_list([1, 2, 3, 2, 6, 4, 5, 6]))

    def test_sum_lists(self):
        # test general
        linked_list_1 = [7, 1, 6]
        linked_list_2 = [5, 9, 2]
        input_head_1 = Node.create_linked_list(linked_list_1)
        input_head_1_copy = Node.create_linked_list(linked_list_1)
        input_head_2 = Node.create_linked_list(linked_list_2)
        input_head_2_copy = Node.create_linked_list(linked_list_2)
        aggregate = sum_lists(input_head_1, input_head_2)
        self.assertEqual(aggregate, 912)

        # ensure linked lists are not modified
        self.assertEqual(input_head_1, input_head_1_copy)
        self.assertEqual(input_head_2, input_head_2_copy)

    def test_palindrome(self):
        # test single
        # linked_list = [1]
        # input_head = Node.create_linked_list(linked_list)
        # self.assertTrue(palindrome(input_head))

        # test double false
        linked_list = [1, 2]
        input_head = Node.create_linked_list(linked_list)
        self.assertFalse(palindrome(input_head))

        # test double true
        linked_list = [2, 2]
        input_head = Node.create_linked_list(linked_list)
        self.assertTrue(palindrome(input_head))

        # test true even
        linked_list = [1, 2, 2, 1]
        input_head = Node.create_linked_list(linked_list)
        self.assertTrue(palindrome(input_head))

        # test true odd
        linked_list = [1, 2, 3, 2, 1]
        input_head = Node.create_linked_list(linked_list)
        self.assertTrue(palindrome(input_head))

        # test false odd
        linked_list = [1, 2, 2, 3, 1]
        input_head = Node.create_linked_list(linked_list)
        self.assertFalse(palindrome(input_head))

        # test false even
        linked_list = [1, 2, 3, 2, 3, 1]
        input_head = Node.create_linked_list(linked_list)
        self.assertFalse(palindrome(input_head))

    def test_intersection(self):
        # different pointer merge
        linked_list_1 = [1, 2, 2, 3, 1]
        input_head_1 = Node.create_linked_list(linked_list_1)
        linked_list_2 = [4, 2, 3, 1]
        input_head_2 = Node.create_linked_list(linked_list_2)
        self.assertIsNone(intersection(input_head_1, input_head_2))

        # same pointer merge
        linked_list_1 = [1, 2, 2, 3, 1]
        input_head_1 = Node.create_linked_list(linked_list_1)
        linked_list_2 = [4, 5]
        input_head_2 = Node.create_linked_list(linked_list_2)
        input_head_2.nextNode.nextNode = input_head_1.nextNode.nextNode.nextNode
        self.assertEqual(intersection(input_head_1, input_head_2), Node.create_linked_list([3, 1]))

    def test_loop_detection_set(self):
        # test general
        linked_list = [1, 2, 3, 4]
        input_head = Node.create_linked_list(linked_list)
        input_head.nextNode.nextNode.nextNode = input_head.nextNode
        self.assertEqual(loop_detection_set(input_head).data, 2)

        # test no loop
        linked_list = [1, 2, 3, 4]
        input_head = Node.create_linked_list(linked_list)
        self.assertIsNone(loop_detection_set(input_head))

    def test_loop_detection_runner_technique(self):
        # test general
        linked_list = [1, 2, 3, 4]
        input_head = Node.create_linked_list(linked_list)
        input_head.nextNode.nextNode.nextNode = input_head.nextNode
        self.assertEqual(loop_detection_runner_technique(input_head).data, 2)

        # test no loop
        linked_list = [1, 2, 3, 4]
        input_head = Node.create_linked_list(linked_list)
        self.assertIsNone(loop_detection_runner_technique(input_head))