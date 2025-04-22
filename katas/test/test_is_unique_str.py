import unittest
from katas.is_unique_str import is_unique

class TestIsUnique(unittest.TestCase):
    def test_hello(self):
        self.assertFalse(is_unique("Hello"))  # so this function assertFalse expect to return False ,  'l' is repeated

    def test_world(self):
        self.assertTrue(is_unique("World"))  # All unique

    def test_python(self):
        self.assertTrue(is_unique("Python"))  # All unique

    def test_unique(self):
        self.assertFalse(is_unique("Unique"))  # 'u' is repeated

    def test_aiman(self):
        self.assertFalse(is_unique("Aiman"))  # 'The letter "a" ' is repeated

    def test_rame(self):
        self.assertTrue(is_unique("Rame"))  # All unique
