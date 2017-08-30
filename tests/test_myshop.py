import unittest
from Designs.main import *

class Myshop(unittest.TestCase):
    '''class defining tests for the myshop application'''
    def test_add_shopping_list_item(self):
        self.assertEqual(add_shopping_list_item(),render_template('add_shopping_list_item.html',records=records)
)