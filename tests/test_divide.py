import unittest

from calc import aec_divide

def broken_function():
    raise Exception("Too many arguments")

class TestDivide(unittest.TestCase):

    def test_divide(self):
        arg_ints = [20,5]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 4)

    def test_cant_divide_by_zero(self):
        arg_ints = [20,0]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 0)

    # this test successfully ran without changing calc.py
    def test_more_than_two_args_general(self):
        self.assertRaises(Exception, aec_divide, 20, 5, 5)
    
    # this test does not work
    def test_more_than_two_args_specific(self):
        with self.assertRaises(Exception, aec_divide, 20, 5, 5) as context:
            broken_function()
    self.assertTrue("Too many arguments" in str(context.exception))

if __name__ == "__main__":
    unittest.main()