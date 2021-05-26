import unittest

from app.qr_functions import keygen


class TestKeygen(unittest.TestCase):
    """
    Class that test the creation of unique identifier.
    """

    def test_len(self):
        uniqueID = keygen.generate_key()
        # test that we have 16^20 different combinations
        self.assertEqual(len(uniqueID), 20)


if __name__ == "__main__":
    unittest.main()
