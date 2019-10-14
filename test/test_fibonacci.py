import unittest
from src.fibonacci import fibonacci


class FibonacciTestCase(unittest.TestCase):

    def test_input_0(self):
        # Arrange
        valid_input_0 = 0
        expected_result = [0]

        # Act
        result = fibonacci(valid_input_0)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_1(self):
        # Arrange
        valid_input_1 = 1
        expected_result = [0, 1]

        # Act
        result = fibonacci(valid_input_1)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_7(self):
        # Arrange
        valid_input_7 = 7
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13]

        # Act
        result = fibonacci(valid_input_7)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_invalid_inputs(self):
        # Arrange
        string_invalid_input = "some_string"
        array_invalid_input = [50, 60]
        none_invalid_input = None
        negative_invalid_input = -1

        # Act and Assert
        self.assertRaises(Exception, fibonacci, string_invalid_input)
        self.assertRaises(Exception, fibonacci, array_invalid_input)
        self.assertRaises(Exception, fibonacci, none_invalid_input)
        self.assertRaises(Exception, fibonacci, negative_invalid_input)


if __name__ == '__main__':
    unittest.main()
