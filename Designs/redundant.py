'''Driver module. All logic in main.py depends on this module for every functionality'''

global account
account=[]
def register(username,email,password):
    '''registration list'''
    account.append(username)
    account.append(email)
    account.append(password)
    return account

global shopping_list_container
shopping_list_container=[]#contain shopping lists only

def create(list_name):
    '''container of names of shopping lists'''
        #list_name=[]
        shopping_list_container.append(list_name)
        return shopping_list_container#list of dictionaries
def list_update(nameoflist,item):
    '''adding item to a given name of list'''
    
    nameoflist.append(item)
    shopping_list_container.append(nameoflist)

global itemsdictionary
itemsdictionary={}
def create1(slist):
    '''update shopping lists with key (names) and items(as dictionaris)'''
    itemsdictionary.update(slist)

global shared_shopping_list_container
shared_shopping_list_container=[]
def create3(list_name):
    '''container for the shared lists. In future may be integrated with facebook'''
        #list_name=[]
        shared_shopping_list_container.append(list_name)
        return shared_shopping_list_container#list of dictionaries

global shareditemsdictionary
shareditemsdictionary={}
def create2(slist):
    '''updating shared dictionary'''
    shareditemsdictionary.update(slist)








