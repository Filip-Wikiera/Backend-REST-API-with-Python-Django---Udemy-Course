from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        resolutin = calc.add(5, 6)

        self.assertEqual(resolutin, 11)

    def test_subtract_numbers(self):
        resolutin = calc.subtract(10, 6)

        self.assertEqual(resolutin, 4)
