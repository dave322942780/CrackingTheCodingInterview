import unittest

from ch4_trees_and_graphs import contains_path_DFS, contains_path_BFS, BinaryNode, create_minimal_depth_tree, \
    lst_of_depths_BFS, check_balanced, successor, validate_BST, build_order, build_order_DFS, first_common_ancestor, \
    BST_sequences, is_subtree, BSTRand, count_paths_sum_to_num_top_bottom, count_paths_sum_to_num_bottom_top, \
    count_paths_sum_to_num_DP
from random import choice, randint


class TreesAndGraphsTestCase(unittest.TestCase):
    def test_contains_path(self):
        ## DFS
        # test no path
        self.assertFalse(contains_path_DFS({
            1: [4, 5],
            2: [3],
            3: [2],
            4: [1, 5],
            5: []
        }, 1, 2))

        # test unidirectional path
        self.assertTrue(contains_path_DFS({
            1: [4, 5],
            2: [3, 4],
            3: [2],
            4: [1, 5],
            5: [1]
        }, 1, 2))

        # test bidirectional path
        self.assertTrue(contains_path_DFS({
            1: [4],
            2: [5, 1],
            3: [2],
            4: [2],
            5: [3]
        }, 1, 5))

        ## BFS
        # test no path
        self.assertFalse(contains_path_BFS({
            1: [4, 5],
            2: [3],
            3: [2],
            4: [1, 5],
            5: []
        }, 1, 2))

        # test unidirectional path
        self.assertTrue(contains_path_BFS({
            1: [4, 5],
            2: [3, 4],
            3: [2],
            4: [1, 5],
            5: [1]
        }, 1, 2))

        # test bidirectional path
        self.assertTrue(contains_path_BFS({
            1: [4],
            2: [5, 1],
            3: [2],
            4: [2],
            5: [3]
        }, 1, 5))

    def test_create_minimal_depth_tree(self):
        # one node
        self.assertEqual(create_minimal_depth_tree([2]), BinaryNode(2))

        # one child only
        actual = create_minimal_depth_tree([2, 3])
        self.assertTrue(actual == BinaryNode(3,
                                             BinaryNode(2))
                        or actual ==
                        BinaryNode(2,
                                   None,
                                   BinaryNode(3)))

        # 2 children
        self.assertEqual(BinaryNode(2, BinaryNode(1), BinaryNode(3)), create_minimal_depth_tree([1, 2, 3]))

        # 3 levels
        self.assertEqual(BinaryNode(4,
                                    BinaryNode(2,
                                               BinaryNode(1),
                                               BinaryNode(3)),
                                    BinaryNode(6,
                                               BinaryNode(5),
                                               BinaryNode(7))),
                         create_minimal_depth_tree([1, 2, 3, 4, 5, 6, 7]))

    def test_lst_of_depths_BFS(self):
        # one node
        self.assertEqual([[1]], lst_of_depths_BFS(BinaryNode(1)))

        # two nodes
        self.assertEqual([[1], [2]], lst_of_depths_BFS(BinaryNode(1,
                                                                  BinaryNode(2))))

        # three nodes
        self.assertEqual([[1], [2, 3]], lst_of_depths_BFS(BinaryNode(1,
                                                                     BinaryNode(2),
                                                                     BinaryNode(3))))

        # unbalanced/un-complete nodes
        self.assertEqual([[1], [2, 3], [4, 5, 6], [7, 8]],
                         lst_of_depths_BFS(
                                 BinaryNode(1,
                                            BinaryNode(2,
                                                       BinaryNode(4),
                                                       BinaryNode(5,
                                                                  BinaryNode(7),
                                                                  BinaryNode(8))),
                                            BinaryNode(3,
                                                       BinaryNode(6)))))

        # balanced/complete nodes
        self.assertEqual([[1], [2, 3], [4, 5, 6, 7]],
                         lst_of_depths_BFS(
                                 BinaryNode(1,
                                            BinaryNode(2,
                                                       BinaryNode(4),
                                                       BinaryNode(5)),
                                            BinaryNode(3,
                                                       BinaryNode(6),
                                                       BinaryNode(7)))))

    def test_check_balanced(self):
        # one node
        self.assertTrue(check_balanced(BinaryNode(1)))

        # two nodes uneven
        self.assertTrue(check_balanced(BinaryNode(1,
                                                  BinaryNode(2))))

        # three nodes uneven
        self.assertTrue(check_balanced(BinaryNode(1,
                                                  BinaryNode(2,
                                                             BinaryNode(3)))))
        # four nodes uneven
        self.assertFalse(check_balanced(BinaryNode(1,
                                                   BinaryNode(2,
                                                              BinaryNode(3,
                                                                         BinaryNode(4))))))
        # six nodes balanced
        self.assertTrue(check_balanced(BinaryNode(1,
                                                  BinaryNode(2,
                                                             BinaryNode(3),
                                                             BinaryNode(4,
                                                                        BinaryNode(5))),
                                                  BinaryNode(6))))
        # eight nodes unbalanced
        self.assertFalse(check_balanced(BinaryNode(1,
                                                   BinaryNode(2,
                                                              BinaryNode(3),
                                                              BinaryNode(4,
                                                                         BinaryNode(5,
                                                                                    BinaryNode(6)))),
                                                   BinaryNode(7))))

    def test_validate_BST(self):
        # one node
        self.assertTrue(check_balanced(BinaryNode(1)))

        # two nodes false
        self.assertTrue(check_balanced(BinaryNode(2,
                                                  None,
                                                  BinaryNode(1))))

        # unbalanced three nodes true
        self.assertTrue(check_balanced(BinaryNode(3,
                                                  None,
                                                  BinaryNode(2,
                                                             None,
                                                             BinaryNode(1)))))
        # 5 nodes, 2 false occurrences
        self.assertFalse(check_balanced(BinaryNode(4,
                                                   None,
                                                   BinaryNode(5,
                                                              None,
                                                              BinaryNode(3,
                                                                         BinaryNode(1),
                                                                         BinaryNode(2))))))
        # 7 nodes, true
        self.assertTrue(validate_BST(BinaryNode(7,
                                                BinaryNode(4,
                                                           BinaryNode(2,
                                                                      BinaryNode(1),
                                                                      BinaryNode(3)),
                                                           BinaryNode(5,
                                                                      None,
                                                                      BinaryNode(6))))))

    def test_successor(self):
        # test single
        self.assertEqual(2, successor(BinaryNode(2, BinaryNode(1)), 1))

        # test general
        bst = BinaryNode(7,
                         BinaryNode(4,
                                    BinaryNode(2,
                                               BinaryNode(1),
                                               BinaryNode(3)),
                                    BinaryNode(5,
                                               None,
                                               BinaryNode(6))))
        for i in range(1, 7):
            self.assertEquals(i + 1, successor(bst, i))

        # test no successor
        self.assertIsNone(successor(bst, 7))

    def test_build_order(self):
        self.assertEqual(build_order([], []), [])
        self.assertEqual(build_order([1], []), [1])

        # one proj with many dependencies
        actual = build_order([1, 2, 3, 4], [[1, 4], [2, 4], [3, 4]])
        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[-1], 4)
        self.assertEqual(set(actual[:3]), {1, 2, 3})

        # test general 4 levels
        #                     9
        #                  7     8
        #                6   3
        #               4 5 1 2
        projs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        projs_copy = projs[:]
        dependencies = [[1, 3], [2, 3], [4, 6], [5, 6], [3, 7], [6, 7], [7, 9], [8, 9]]
        dependencies_copy = [dependency[:] for dependency in dependencies]
        actual = build_order(projs, dependencies)
        self.assertEqual(len(projs), len(actual))
        self.assertEqual(set(projs), set(actual))
        self.assertEqual(dependencies, dependencies_copy)
        self.assertEqual(projs, projs_copy)
        for dependency in dependencies:
            self.assertLess(actual.index(dependency[0]), actual.index(dependency[1]))

        # test error:
        try:
            projs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            dependencies = [[1, 3], [2, 3], [4, 6], [5, 6], [3, 7], [6, 7], [7, 9], [9, 4]]
            actual = build_order(projs, dependencies)
            self.fail("no exception raised")
        except:
            pass

        self.assertEqual(build_order_DFS([], []), [])
        self.assertEqual(build_order_DFS([1], []), [1])

        # one proj with many dependencies
        actual = build_order_DFS([1, 2, 3, 4], [[1, 4], [2, 4], [3, 4]])
        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[-1], 4)
        self.assertEqual(set(actual[:3]), {1, 2, 3})

        # test general 4 levels
        #                     9
        #                  7     8
        #                6   3
        #               4 5 1 2
        projs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        projs_copy = projs[:]
        dependencies = [[1, 3], [2, 3], [4, 6], [5, 6], [3, 7], [6, 7], [7, 9], [8, 9]]
        dependencies_copy = [dependency[:] for dependency in dependencies]
        actual = build_order_DFS(projs, dependencies)
        self.assertEqual(len(projs), len(actual))
        self.assertEqual(set(projs), set(actual))
        self.assertEqual(dependencies, dependencies_copy)
        self.assertEqual(projs, projs_copy)
        for dependency in dependencies:
            self.assertLess(actual.index(dependency[0]), actual.index(dependency[1]))

        # test error:
        try:
            projs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            dependencies = [[1, 3], [2, 3], [4, 6], [5, 6], [3, 7], [6, 7], [7, 9], [9, 4]]
            actual = build_order_DFS(projs, dependencies)
            self.fail("no exception raised")
        except:
            pass

    def test_first_common_ancestor(self):

        tree = BinaryNode(1,
                          BinaryNode(2,
                                     BinaryNode(3),
                                     BinaryNode(4,
                                                BinaryNode(5,
                                                           BinaryNode(6)))),
                          BinaryNode(7))

        # test diverge path
        self.assertEqual(first_common_ancestor(tree.left.left, tree.left.right.left.left, tree), tree.left)
        # test ancestor of another
        self.assertEqual(first_common_ancestor(tree.left, tree.left.right.left.left, tree), tree.left)
        # test not found
        self.assertIsNone(first_common_ancestor(BinaryNode(8), tree.left.right.left.left, tree))
        # test different object same value
        self.assertIsNone(first_common_ancestor(BinaryNode(tree.left.data), tree.left.right.left.left, tree))

    def test_BST_sequences(self):
        # test tress with 1 or 2 nodes
        self.assertEqual([[1]], BST_sequences(BinaryNode(1)))
        self.assertEqual([[2, 1]], BST_sequences(BinaryNode(2, BinaryNode(1))))

        actual_seqs = BST_sequences(BinaryNode(2, BinaryNode(1), BinaryNode(4, BinaryNode(3))))
        expected_seqs = [[2, 4, 3, 1], [2, 4, 1, 3], [2, 1, 4, 3]]
        for expected_seq in expected_seqs:
            self.assertIn(expected_seq, actual_seqs)

        actual_seqs = BST_sequences(BinaryNode(2, BinaryNode(1), BinaryNode(4, BinaryNode(3), BinaryNode(5))))
        expected_seqs = [[2, 4, 5, 3, 1], [2, 4, 5, 1, 3], [2, 4, 1, 5, 3], [2, 1, 4, 5, 3],
                         [2, 4, 3, 5, 1], [2, 4, 3, 1, 5], [2, 4, 1, 3, 5], [2, 1, 4, 3, 5]]
        for expected_seq in expected_seqs:
            self.assertIn(expected_seq, actual_seqs)

    def test_is_subtree(self):

        # test 1 node identical/true
        tree = BinaryNode(1)
        tree_cpy = BinaryNode(1)
        self.assertTrue(is_subtree(tree, tree_cpy))

        # test 1 node subtree of second/true
        tree = BinaryNode(2, BinaryNode(1))
        subtree = BinaryNode(1)
        self.assertTrue(is_subtree(tree, subtree))

        # test top half identical only/false
        tree = BinaryNode(2, BinaryNode(1), BinaryNode(3, BinaryNode(4)))
        subtree = BinaryNode(2, BinaryNode(1), BinaryNode(3))
        self.assertFalse(is_subtree(tree, subtree))

        # test identical/true
        tree = BinaryNode(1,
                          BinaryNode(5,
                                     BinaryNode(2),
                                     BinaryNode(3)),
                          BinaryNode(6,
                                     BinaryNode(9),
                                     BinaryNode(8)))
        tree_cpy = BinaryNode(1,
                              BinaryNode(5,
                                         BinaryNode(2),
                                         BinaryNode(3)),
                              BinaryNode(6,
                                         BinaryNode(9),
                                         BinaryNode(8)))
        self.assertTrue(is_subtree(tree, tree_cpy))

        # test general subtree/true
        tree = BinaryNode(1,
                          BinaryNode(5,
                                     BinaryNode(2),
                                     BinaryNode(3)),
                          BinaryNode(6,
                                     BinaryNode(9),
                                     BinaryNode(8)))
        tree_cpy = BinaryNode(5,
                              BinaryNode(2),
                              BinaryNode(3))
        self.assertTrue(is_subtree(tree, tree_cpy))
        # test general subtree/false
        tree = BinaryNode(1,
                          BinaryNode(5,
                                     BinaryNode(2),
                                     BinaryNode(3)),
                          BinaryNode(6,
                                     BinaryNode(9),
                                     BinaryNode(8)))
        tree_cpy = BinaryNode(6,
                              BinaryNode(2),
                              BinaryNode(3))
        self.assertFalse(is_subtree(tree, tree_cpy))

    def test_BSTRand(self):
        # white box testing

        def test_parent(node):
            if node.left:
                self.assertEqual(id(node.left.parent), id(node))
                test_parent(node.left)
            if node.right:
                self.assertEqual(id(node.right.parent), id(node))
                test_parent(node.right)

        def get_inorder(node, lst=[]):
            ret = False
            if not lst:
                ret = True

            if not node:
                return
            if node.left:
                get_inorder(node.left, lst)
            lst.append(node.data)
            if node.right:
                get_inorder(node.right, lst)

            if ret:
                return lst

        # test bst insert
        bst = BSTRand(2)
        bst.insert(1)
        bst.insert(4)
        bst.insert(6)
        bst.insert(5)
        bst.insert(3)
        test_parent(bst)
        self.assertEqual(2, bst.data)
        self.assertEqual(1, bst.left.data)
        self.assertEqual(4, bst.right.data)
        self.assertEqual(3, bst.right.left.data)
        self.assertEqual(6, bst.right.right.data)
        self.assertEqual(5, bst.right.right.left.data)
        self.assertEqual(6, bst.size)
        self.assertEqual(1, bst.left.size)
        self.assertEqual(4, bst.right.size)
        self.assertEqual(1, bst.right.left.size)
        self.assertEqual(2, bst.right.right.size)
        self.assertEqual(1, bst.right.right.left.size)
        self.assertIsNone(bst.left.left)
        self.assertIsNone(bst.left.right)
        self.assertIsNone(bst.right.left.right)
        self.assertIsNone(bst.right.left.left)
        self.assertIsNone(bst.right.right.right)
        self.assertIsNone(bst.right.right.left.left)
        self.assertIsNone(bst.right.right.left.right)

        # test bst delete
        self.assertTrue(bst.delete(4))
        self.assertTrue(bst.delete(5))
        self.assertTrue(bst.delete(3))
        test_parent(bst)
        self.assertEqual(2, bst.data)
        self.assertEqual(1, bst.left.data)
        self.assertEqual(6, bst.right.data)
        self.assertIsNone(bst.left.left)
        self.assertIsNone(bst.left.right)
        self.assertIsNone(bst.right.left)
        self.assertIsNone(bst.right.right)
        self.assertEqual(3, bst.size)
        self.assertEqual(1, bst.left.size)
        self.assertEqual(1, bst.right.size)

        # test delete from an empty tree
        self.assertTrue(bst.delete(6))
        self.assertTrue(bst.delete(1))
        try:
            bst.delete(2)
            self.fail("Able to remove the last node in a tree")
        except:
            pass

        # test insert
        bst = None
        node_data = range(100)
        for i in range(100):
            idx_to_rm = randint(0, 100 - i - 1)
            if i == 0:
                bst = BSTRand(node_data.pop(idx_to_rm))
            else:
                bst.insert(node_data.pop(idx_to_rm))
        self.assertEqual(100, bst.size)
        self.assertEqual(range(100), get_inorder(bst))
        test_parent(bst)

        # test get_random_node, delete, and implicitly *find
        node_data = range(100)
        for i in range(99):
            idx_to_rm = randint(1, 100 - i)
            # optional parameter idx_to_rm for white box testing
            rand_node_val = bst.get_random_node(idx_to_rm)
            self.assertEqual(node_data.pop(idx_to_rm - 1), rand_node_val)
            self.assertTrue(bst.delete(rand_node_val))

    def test_count_paths_sum_to_num(self):

        # single node with path
        bt = BinaryNode(2)
        self.assertEqual(1, count_paths_sum_to_num_top_bottom(bt, 2))

        # single node without path
        self.assertEqual(0, count_paths_sum_to_num_top_bottom(bt, 3))

        # multi node multi paths with overlaps
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_top_bottom(bt, 6))

        # multi node no path
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(0, count_paths_sum_to_num_top_bottom(bt, 13))

        # multi node multi paths with overlaps and negative numbers
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(-2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_top_bottom(bt, 4))


        # single node with path
        bt = BinaryNode(2)
        self.assertEqual(1, count_paths_sum_to_num_bottom_top(bt, 2))

        # single node without path
        self.assertEqual(0, count_paths_sum_to_num_bottom_top(bt, 3))

        # multi node multi paths with overlaps
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_bottom_top(bt, 6))

        # multi node no path
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(0, count_paths_sum_to_num_bottom_top(bt, 13))

        # multi node multi paths with overlaps and negative numbers
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(-2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_bottom_top(bt, 4))


        # single node with path
        bt = BinaryNode(2)
        self.assertEqual(1, count_paths_sum_to_num_DP(bt, 2))

        # single node without path
        self.assertEqual(0, count_paths_sum_to_num_DP(bt, 3))

        # multi node multi paths with overlaps
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_DP(bt, 6))


        # multi node no path
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(2), BinaryNode(6)))
        self.assertEqual(0, count_paths_sum_to_num_DP(bt, 13))

        # multi node multi paths with overlaps and negative numbers
        bt = BinaryNode(2, BinaryNode(1, BinaryNode(4), BinaryNode(3)), BinaryNode(4, BinaryNode(-2), BinaryNode(6)))
        self.assertEqual(4, count_paths_sum_to_num_DP(bt, 4))
