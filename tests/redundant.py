'''Due to the needs arising from completing the project on time, I have defined redundant.py
which will hold replacement modules as I migrate from file based application to lists only web application. This modules
so far will offer the capabilities of registration, creating a shopping list and adding items into
a shopping list'''

global account
account=[]
def register(username,email,password):
    if type(username)!=str or type(email)!=str:
        raise TypeError('Name can not be a digit combination')
    else:
        account.append(username)
        account.append(email)
        account.append(password)
        return account

global shopping_list_container
shopping_list_container=[]

def create(list_name):
        
        list_name=[]
        shopping_list_container.append(list_name)
        return shopping_list_container
def list_update(nameoflist,item):
    if nameoflist in shopping_list_container:
        nameoflist.append(item)
        shopping_list_container.append(nameoflist)







