import unittest
from src.adder import add


class AdderTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11, "Should be 11")

    def test_add_exception(self):
        self.assertRaises(Exception, add, "1", "2")


if __name__ == '__main__':
    unittest.main()
