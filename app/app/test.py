from django.test import TestCase

from app.calc import add, substract


class CalcTest(TestCase):

    def test_add_number(self):
        """Test the two number are added together"""
        self.assertEqual(add(1, 3), 4)
    def test_subtract_number(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(substract(5, 3), 2)