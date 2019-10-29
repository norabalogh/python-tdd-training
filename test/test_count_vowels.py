import unittest
from src.count_vowels import count_vowels


class CountVowelsTestCase(unittest.TestCase):

    def test_valid_input(self):
        # Arrange
        valid_input = "Hello World"
        expected_result = 3

        # Act
        result = count_vowels(valid_input)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_invalid_input(self):
        # Arrange
        invalid_input = [3, 45, 6]

        # Act and Assert
        self.assertRaises(Exception, count_vowels, invalid_input)


if __name__ == '__main__':
    unittest.main()
