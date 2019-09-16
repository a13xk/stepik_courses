import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(first=abs(-42), second=42, msg="Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(first=abs(-42), second=-42, msg="Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
