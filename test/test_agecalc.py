import unittest
from datetime import datetime, date
from src.agecalc import agecalc


class AgeCalcTestCase(unittest.TestCase):

    def test_input_0(self):
        # Arrange
        today = date.today()
        tested_year = today.year - 22
        valid_input_0 = str(tested_year) + " 03 21"
        expected_result = 22

        # Act
        result = agecalc(valid_input_0)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_1(self):
        # Arrange
        today = date.today()
        tested_year = today.year - 1
        valid_input_1 = str(tested_year) + " 10 19"
        expected_result = 1

        # Act
        result = agecalc(valid_input_1)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_2(self):
        # Arrange
        today = date.today()
        tested_year = today.year
        valid_input_2 = str(tested_year) + " 10 21"
        expected_result = 0

        # Act
        result = agecalc(valid_input_2)

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
        self.assertRaises(Exception, agecalc, string_invalid_input)
        self.assertRaises(Exception, agecalc, array_invalid_input)
        self.assertRaises(Exception, agecalc, none_invalid_input)
        self.assertRaises(Exception, agecalc, negative_invalid_input)


if __name__ == '__main__':
    unittest.main()
