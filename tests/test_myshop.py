import unittest
import urllib
from flask_testing import LiveServerTestCase
from flask_testing import TestCase
from flask import Flask
from Designs.main import *



class Myshop(TestCase):
    '''class defining tests for the myshop application'''
    render_templates = False
    def create_app(self):
        app==Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        #set to zero to allow OS to choose which port to use
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app
    def test_assert_not_process_the_template(self):
        response = self.client.get("templates/")

        assert "" != response.data

    def test_assert_mytemplate_used(self):
        response = self.client.get("templates/")

        self.assert_template_used('add_shopping_list_item.html')

    
if __name__=='__main__':
    unittest.main()
