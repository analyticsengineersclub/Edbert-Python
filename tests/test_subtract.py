import unittest

from calc import aec_subtract


def broken_function():
    raise Exception("Too many arguments")


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        arg_ints = [20, 5]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 15)

    def test_cant_go_below_zero(self):
        arg_ints = [5, 20]
        sub_result = aec_subtract(arg_ints)
        self.assertEqual(sub_result, 0)

    def test_more_than_two_args(self):
        self.assertRaises(Exception, aec_subtract, 20, 5, 5)


if __name__ == "__main__":
    unittest.main()
