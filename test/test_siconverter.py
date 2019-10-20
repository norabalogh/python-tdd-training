import unittest
from src.siconverter import siconverter


class SiConverterTestCase(unittest.TestCase):

    def test_input_m(self):
        # Arrange
        valid_val = 1
        valid_unit_in = 'm'
        valid_unit_out = 'km'
        expected_result = 0.001

        # Act
        result = siconverter(valid_val, valid_unit_in, valid_unit_out)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_input_km(self):
        # Arrange
        valid_val = 1
        valid_unit_in = 'km'
        valid_unit_out = 'm'
        expected_result = 1000.0

        # Act
        result = siconverter(valid_val, valid_unit_in, valid_unit_out)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_invalid_inputs(self):
        # Act and Assert
        self.assertRaises(Exception, siconverter, 'm', 'm',
                          'm')  # how to add here more inputs?


if __name__ == '__main__':
    unittest.main()
