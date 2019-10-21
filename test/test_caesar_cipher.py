import unittest
from src.caesar_cipher import encrpyt
from src.caesar_cipher import decrypt


class CaesarCipherTestCase(unittest.TestCase):

    def test_encrpyt(self):
        # Arrange
        valid_input = "Very secret message!44"
        expected_result = "Yhub vhfuhw phvvdjh!44"

        # Act
        result = encrpyt(valid_input)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))

    def test_decrypt(self):
        # Arrange
        valid_input = "Yhub vhfuhw phvvdjh!44"
        expected_result = "Very secret message!44"

        # Act
        result = decrypt(valid_input)

        # Assert
        self.assertEqual(result, expected_result,
                         "Result should be " + str(expected_result))


if __name__ == '__main__':
    unittest.main()
