import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(7), "Childe")