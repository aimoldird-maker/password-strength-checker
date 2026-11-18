
import unittest
from main import check_password


class TestPasswordChecker(unittest.TestCase):

    def test_strong_password(self):
        checks, strength = check_password("MyTestPass123!")
        self.assertEqual(strength, "STRONG")

    def test_medium_password(self):
        checks, strength = check_password("Hello1234567")
        self.assertEqual(strength, "MEDIUM")

    def test_weak_password(self):
        checks, strength = check_password("abc")
        self.assertEqual(strength, "WEAK")

    def test_common_password(self):
        checks, strength = check_password("password123")
        self.assertEqual(strength, "WEAK")


if __name__ == "__main__":
    unittest.main()
