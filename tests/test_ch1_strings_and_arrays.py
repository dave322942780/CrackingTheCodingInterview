import unittest

from ch1_strings_and_arrays import is_unique_1_1, is_unique_bit_array_1_1, is_permutation_1_2, URLify_1_3, \
    palindrome_permutation_1_4, one_way_1_5, string_compression_1_6, rotate_matrix_1_7, zero_matrix_1_8, \
    string_rotation_1_9
from ch3_stacks_and_queues import Stack


class StringMethodsTestCase(unittest.TestCase):
    def test_is_unique(self):
        # test simple true false
        self.assertTrue(is_unique_1_1("aewsfdxv"))
        self.assertFalse(is_unique_1_1("aewsfdxve"))

    def test_is_unique_vector(self):
        # test simple true false
        self.assertTrue(is_unique_bit_array_1_1("aewsfdxv"))
        self.assertFalse(is_unique_bit_array_1_1("aewsfdxve"))

    def test_anagram_substring(self):
        # test single letter
        # self.assertTrue(is_permutation_1_2("a", "adsgbaacariojgw"))

        # test same size strings
        self.assertTrue(is_permutation_1_2("abbc", "bacb"))

        # test simple true false
        self.assertTrue(is_permutation_1_2("adsgbaacariojgw", "aabc"))
        self.assertFalse(is_permutation_1_2("aabc", "adsgbacriojgw"))

    def test_URLify(self):
        # test empty
        self.assertEqual(URLify_1_3(""), "")

        # single space
        self.assertEqual(URLify_1_3(" "), "%%20")

        # test general
        self.assertEqual(URLify_1_3("I want   you"), "I%%20want%%20%%20%%20you")

    def test_palindrome_permutation(self):
        # test odd num of chars
        self.assertTrue(palindrome_permutation_1_4("asdf fdas"))

        # test even num of chars
        self.assertTrue(palindrome_permutation_1_4("asdffdas"))

        # test false
        self.assertFalse(palindrome_permutation_1_4("asf fdas"))

    def test_one_way(self):
        # test general true
        self.assertTrue(one_way_1_5("pale", "ple"))
        self.assertTrue(one_way_1_5("pales", "pale"))
        self.assertTrue(one_way_1_5("pale", "bale"))

        # test false
        self.assertFalse(one_way_1_5("pale", "bake"))

    def test_string_compression(self):
        # test same size
        self.assertEqual("abccdd", string_compression_1_6("abccdd"))

        # test different size general
        self.assertEqual("abc3d3ada", string_compression_1_6("abcccdddada"))

    def test_rotate_matrix(self):
        # test 3*3
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sol = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        rotate_matrix_1_7(matrix)
        self.assertEqual(sol, matrix)

        # test 4*4
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        sol = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        rotate_matrix_1_7(matrix)
        self.assertEqual(sol, matrix)

    def test_zero_matrix(self):
        # test no zeros
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        sol = [row[:] for row in matrix]
        zero_matrix_1_8(matrix)
        self.assertEqual(sol, matrix)

        # test zeros same row
        matrix = [[1, 2, 3, 4], [5, 6, 0, 0], [9, 10, 11, 12], [13, 14, 15, 16]]
        sol = [[1, 2, 0, 0], [0, 0, 0, 0], [9, 10, 0, 0], [13, 14, 0, 0]]
        zero_matrix_1_8(matrix)
        self.assertEqual(sol, matrix)

        # test general
        matrix = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        sol = [[1, 2, 0, 0], [0, 0, 0, 0], [9, 10, 0, 0], [0, 0, 0, 0]]
        zero_matrix_1_8(matrix)
        self.assertEqual(sol, matrix)

    def test_rotate_string(self):
        # test general
        self.assertTrue(string_rotation_1_9("waterbottle", "rbottlewate"))

        # test one char beginnging
        self.assertTrue(string_rotation_1_9("waterbottle", "ewaterbottl"))

        # test one char ending
        self.assertTrue(string_rotation_1_9("waterbottle", "aterbottlew"))

        # test identical
        self.assertTrue(string_rotation_1_9("waterbottle", "waterbottle"))

        # test different size
        self.assertFalse(string_rotation_1_9("waterbottle", "waterbot"))

        # test false
        self.assertFalse(string_rotation_1_9("waterbottle", "watottleerb"))

