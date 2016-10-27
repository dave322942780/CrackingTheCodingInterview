import random
import unittest

from ch8_recursion_dynamic_programming import triple_step, robot_in_grid, magic_idx, power_set, recursive_multiply, \
    towers_of_hanoi, permutation_without_dups, permutation_without_dups_2, parens, paint_fill


class RecursionDynamicProgramming(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(1, triple_step(1))
        self.assertEqual(2, triple_step(2))
        self.assertEqual(4, triple_step(3))
        self.assertEqual(7, triple_step(4))
        self.assertEqual(13, triple_step(5))

    def test_robot_in_grid(self):
        self.assertEqual(robot_in_grid([[0, 1, 0],
                                        [0, 0, 0],
                                        [1, 1, 0]]),
                         [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])
        self.assertIsNone(robot_in_grid([[0, 1, 0],
                                         [0, 1, 0],
                                         [1, 1, 0]]))

    def test_magic_idx(self):
        self.assertEqual(2, magic_idx([-10, -1, 2, 5]))
        self.assertEqual(3, magic_idx([-10, -1, 1, 3]))
        self.assertEqual(0, magic_idx([0, 2, 4, 8]))
        self.assertEqual(2, magic_idx([0, 2, 2, 2]))

    def test_power_set(self):
        actual = power_set({1, 2, 3})
        for i in [{}, {3}, {2, 3}, {2}, {1, 2}, {1, 2, 3}, {1, 3}, {1}]:
            self.assertIn(i, actual)

    def test_recursive_multiply(self):

        for i in range(100):
            n1, n2 = random.sample(range(1000), 2)
            self.assertEqual(n1 * n2, recursive_multiply(n1, n2))

    def test_towers_of_hanoi(self):
        for i in range(2, 10):
            stack = [None, range(i, 0, -1), [], []]
            moves = towers_of_hanoi(i)
            moves.reverse()
            while moves:
                size, from_tower, to_tower = moves.pop()
                self.assertIsNotNone(stack[from_tower])
                self.assertEqual(size, stack[from_tower][-1])
                stack[from_tower].pop()
                if stack[to_tower]:
                    self.assertLess(size, stack[to_tower][-1])
                stack[to_tower].append(size)
            expected_stack = [None, [], [], range(i, 0, -1)]
            self.assertEqual(stack, expected_stack)

    def test_string_permutation_without_dups(self):
        abcd_permutations = ['dbac', 'bdac', 'badc', 'bacd', 'dbca',
                             'bdca', 'bcda', 'bcad', 'dcba', 'cdba',
                             'cbda', 'cbad', 'dabc', 'adbc', 'abdc',
                             'abcd', 'dacb', 'adcb', 'acdb', 'acbd',
                             'dcab', 'cdab', 'cadb', 'cabd']
        self.assertEqual([""], permutation_without_dups(''))
        self.assertEqual([""], permutation_without_dups_2(''))
        self.assertEqual(["1"], permutation_without_dups('1'))
        self.assertEqual(["1"], permutation_without_dups_2('1'))
        for permutation in abcd_permutations:
            self.assertEqual(set(abcd_permutations), set(permutation_without_dups(permutation)))
        for permutation in abcd_permutations:
            self.assertEqual(set(abcd_permutations), set(permutation_without_dups_2(permutation)))

    def test_permutation_with_dups(self):
        aabb_permutations = ['aacbb', 'aabcb', 'aabbc', 'acabb', 'acbab', 'acbba',
                             'abacb', 'ababc', 'abcab', 'abcba', 'abbac', 'abbca',
                             'caabb', 'cabab', 'cabba', 'cbaab', 'cbaba', 'cbbaa',
                             'baacb', 'baabc', 'bacab', 'bacba', 'babac', 'babca',
                             'bcaab', 'bcaba', 'bcbaa', 'bbaac', 'bbaca', 'bbcaa']
        self.assertEqual([""], permutation_without_dups(''))
        self.assertEqual([""], permutation_without_dups_2(''))
        self.assertEqual(["aa"], permutation_without_dups('aa'))
        self.assertEqual(["aa"], permutation_without_dups_2('aa'))
        for permutation in aabb_permutations:
            self.assertEqual(set(aabb_permutations), set(permutation_without_dups(permutation)))
        for permutation in aabb_permutations:
            self.assertEqual(set(aabb_permutations), set(permutation_without_dups_2(permutation)))

    def test_parens(self):
        self.assertEqual(["()"], parens(1))
        expected = {'(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
                    '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'}
        self.assertEqual(expected, set(parens(4)))

    def test_fill_painting(self):
        self.assertEqual([["a"]], paint_fill([["c"]], 0, 0, "a"))

        painting = [["c", "c", "c"],
                    ["e", "b", "b"],
                    ["d", "d", "d"]]
        painting_copy = [p[:] for p in painting]
        actual = paint_fill(painting, 0, 0, "a")
        self.assertEqual(painting_copy, painting)
        expected = [['a', 'a', 'a'],
                    ['e', 'b', 'b'],
                    ['d', 'd', 'd']]
        self.assertEqual(expected, actual)
        actual = paint_fill(painting, 0, 1, "a")
        expected = [['c', 'c', 'c'],
                    ['a', 'b', 'b'],
                    ['d', 'd', 'd']]
        self.assertEqual(expected, actual)
        painting = [['c', 'c', 'c'],
                    ['c', 'a', 'c'],
                    ['a', 'c', 'c']]
        actual = paint_fill(painting, 0, 0, "d")
        expected = [['d', 'd', 'd'],
                    ['d', 'a', 'd'],
                    ['a', 'd', 'd']]
        self.assertEqual(expected, actual)
