from django.test import TestCase

from .units import add_3_numbers

class Add_3_Numbers_TestCase(TestCase):
    def test_add_three_number(self):
        result = add_3_numbers(5, 4, 3)
        self.assertEqual(result, 13)