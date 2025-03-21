import unittest
from main import hello

class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")
        self.assertEqual(hello("Alice"), "Hello, Alice!")
        self.assertEqual(hello("Bob"), "Hello, Bob!")

if __name__ == "__main__":
    unittest.main()