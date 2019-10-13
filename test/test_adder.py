import unittest
from src.Adder import add


class TestAdder(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11, "Should be 11")

    def test_ad(self):
        self.assertEqual(add(5, 6), 11, "Should be 11")


if __name__ == '__main__':
    unittest.main()
