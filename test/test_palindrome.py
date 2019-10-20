import unittest
from src.palindrome import is_palindrome


class PalindromeTestCase(unittest.TestCase):

    def test_palindrome_true(self):
        # Arrange
        checked_str = "tacocat"
        expected_result = True

        # Act
        result = is_palindrome(checked_str)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_palindrome_false(self):
        # Arrange
        checked_str = "not a palindrome"
        expected_result = False

        # Act
        result = is_palindrome(valid_input_1)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))


if __name__ == '__main__':
    unittest.main()
