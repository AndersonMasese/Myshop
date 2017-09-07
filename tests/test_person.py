import unittest
from app.person import *


class ThisPerson(unittest.TestCase):
    def test_register_returns_list(self):
        '''test that when user enters their registration details, 
        they are stored in a list object'''
        a = 'anderson'
        b = 'kenyanya'
        c = 'andersonkenyanya'
        self.assertIsInstance(register(a, b, c), list,
                              msg='method register has not returned list object')

    def test_doesnt_accept_integer_names(self):
        '''test that the registration method doesnt accept integers'''
        self.assertEqual(register(1,'anderson','masese'),'only strings allowed for names')

    def test_account_list_holds_three_values(self):
        '''test if the items in the shopping list are three'''
        self.assertEqual(len(registration('ANDERSON','MASESE','ONSANDO')),3)

    def test_login_function_returns_list(self):
        '''ensure that the login function returns a list of user credentials'''
        self.assertIsInstance(login(),list)

    def test_register_not_duplicated(self):
        '''test that people do not insert their registration details more than once'''
        temp_list=Person.account
        register('Johann','MARK','GRACIOUS')
        if 'MARK' in temp_list:
            self.assertEqual(register('Johann','MARK','GRACIOUS'),'you are aready registered')



if __name__ == '__main__':
    unittest.main()
