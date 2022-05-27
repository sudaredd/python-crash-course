import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Sudar', 'Kasir')
        self.assertEqual(formatted_name, 'Sudar Kasir')
        self.assertFalse(formatted_name=='SudarKasir')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Sudar', 'Kasir', "Rd")
        self.assertEqual(formatted_name, 'Sudar Rd Kasir')
        self.assertFalse(formatted_name == 'Sudar R Kasir')

unittest.main()