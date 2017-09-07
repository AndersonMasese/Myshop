'''This module executes the shop list characteristics as executed in main file'''
from .person import Person


class ShoppingList(Person):
    '''methods  for manipulating ShoppingList'''
    itemsdictionary = {}
    shopping_list_container = []

    def add_items(self):
        '''return dictionary of items'''
        return self.itemsdictionary

    def add_shopping_list(self):
        return self.shopping_list_container

    def create(self, list_name):
        return self.shopping_list_container.append(list_name)

    def create1(self, shopping_list):
        '''should return dictionary containing name:item'''
        return self.itemsdictionary.update(shopping_list)
