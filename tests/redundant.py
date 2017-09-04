'''module for exposing functionality logic for main.py'''

global account
account = []


def register(username, email, password):
    account.append(username)
    account.append(email)
    account.append(password)
    return account


global shopping_list_container
shopping_list_container = []  # contain shopping lists only


def create(list_name):
    # list_name=[]
    shopping_list_container.append(list_name)
    return shopping_list_container  # list of dictionaries


def list_update(nameoflist, item):

    nameoflist.append(item)
    shopping_list_container.append(nameoflist)


global itemsdictionary
itemsdictionary = {}


def create1(slist):
    itemsdictionary.update(slist)


global shared_shopping_list_container
shared_shopping_list_container = []


def create3(list_name):
    # list_name=[]
    shared_shopping_list_container.append(list_name)
    return shared_shopping_list_container  # list of dictionaries


global shareditemsdictionary
shareditemsdictionary = {}


def create2(slist):
    shareditemsdictionary.update(slist)
