import unittest

from ch5_bit_manipulation import insertion, binary_to_str


class BitManipulationTestCase(unittest.TestCase):
    def test_insertion(self):
        orig = int('10000000000', 2)
        replace = int('10011', 2)
        start_idx = 2
        end_idx = 6

        self.assertEqual(int('10001001100', 2), insertion(orig, replace, start_idx, end_idx))

    def test_binary_to_string(self):
        self.assertEqual("0.1", binary_to_str(0.5))
        self.assertEqual("0.11", binary_to_str(0.75))
        self.assertEqual("0.101", binary_to_str(0.625))

        # test longer than 32 digits
        try:
            binary_to_str(0.3)
            self.fail("Should be longer than 32 consecutive digits, no error was raised")
        except Exception:
            pass
