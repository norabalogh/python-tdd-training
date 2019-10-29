import unittest
from src.is_anagram import is_anagram


class IsAnagramTestCase(unittest.TestCase):

    def test_input_anagrams_cat_act(self):
        # Arrange
        param1 = "cat"
        param2 = "act"
        expected_result = True

        # Act
        result = is_anagram(param1, param2)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_anagrams_low_owl(self):
        # Arrange
        param1 = "low"
        param2 = "owl"
        expected_result = True

        # Act
        result = is_anagram(param1, param2)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_not_anagrams(self):
        # Arrange
        param1 = "horse"
        param2 = "goat"
        expected_result = False

        # Act
        result = is_anagram(param1, param2)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))


if __name__ == '__main__':
    unittest.main()
