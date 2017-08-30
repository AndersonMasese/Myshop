import unittest
import urllib
from flask_testing import LiveServerTestCase
from flask_testing import TestCase
from flask import Flask
from Designs.main import *
from redundant import *



class Myshop(TestCase):
    '''class defining tests for the myshop application'''
    render_templates = False
    def create_app(self):
        app==Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        #set to zero to allow OS to choose which port to use
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app
    def setup(self):
        self.entries=3

    def test_assert_not_process_the_template(self):
        response = self.client.get("templates/")

        assert "" != response.data
    def test_redundant_register_returns_list_object(self):
        '''test that when user enters their registration details, 
        they are stored in a list object'''
        a='anderson'
        b='kenyanya'
        c='andersonkenyanya'
        self.assertIsInstance(register(a,b,c),list,msg='method register has not returned list object')

    def test_redundant_returns_correct_num_of_entrie(self):
        '''method to ensure variables are not added to list automagically'''
        temp_length=register('a','b','c')
        self.assertEqual(len(temp_length),6,msg='All three fields in register need to be filled out')

    def test_data_integrity(self):
        '''ensure one does not enter digits as names of people during registration'''
        name=900
        email=89.0
        password='password'
        self.assertRaises(TypeError,'Name can not be a digit combination')

    def test_register_appends_items(self):
        '''test if the register function appends entered details into a list'''
        temp_list=register('a','b','c')
        self.assertIn('a',temp_list)

    #def test_create_return_list_of_lists(self):
        #'''Ensure that creating a room returns a list containing other lists'''





    

    
if __name__=='__main__':
    unittest.main()
