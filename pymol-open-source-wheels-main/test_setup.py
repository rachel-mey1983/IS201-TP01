import unittest

class DummyTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True, "Should always be True")

if __name__ == '__main__':
    unittest.main()