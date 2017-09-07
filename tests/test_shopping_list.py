import unittest
from app.shoppinglist import *


class ThisPerson(unittest.TestCase):
    '''class holding tests for shopping list class'''
    def test_add_item_return_list(self):
        '''test if method returns a dictionary instance'''
        self.assertIsInstance(add_items(),{},msg='method returning a dictionary instance')


if __name__ == '__main__':
    unittest.main()
