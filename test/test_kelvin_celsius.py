import unittest
from src.kelvin_celsius import kelvin_to_celsius
from src.kelvin_celsius import celsius_to_kelvin


class KelvinToCelsiusTestCase(unittest.TestCase):

    def test_kelvin_to_celsius_valid_input(self):
        # Arrange
        kelvin = 256
        expected_celsius = -17.15

        # Act
        result = kelvin_to_celsius(kelvin)

        # Assert
        self.assertAlmostEqual(result, expected_celsius, 1,
                               "Result should be " + str(expected_celsius))

    def test_kelvin_to_celsius_invalid_input(self):
        # Arrange
        kelvin = -80
        string = "TestStr"

        # Act & Assert
        self.assertRaises(Exception, kelvin_to_celsius, kelvin)
        self.assertRaises(Exception, kelvin_to_celsius, string)

    def test_celsius_to_kelvin_valid_input(self):
        # Arrange
        celsius = 150
        expected_kelvin = 423.15

        # Act
        result = celsius_to_kelvin(celsius)

        # Assert
        self.assertEqual(result, expected_kelvin,
                         "Result should be " + str(expected_kelvin))

    def test_celsius_to_kelvin_invalid_input(self):
        # Arrange
        celsius = -5000
        string = "TestStr"

        # Act & Assert
        self.assertRaises(Exception, celsius_to_kelvin, celsius)
        self.assertRaises(Exception,
                          celsius_to_kelvin, string)


if __name__ == '__main__':
    unittest.main()
