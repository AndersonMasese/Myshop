from person import Person

class ShoppingList(Person):
    '''class models the creation of a shopping list and logging of users to a local file
    for purposes of sharing shopping lists'''

    
    def create(self,list_name,description):
        '''This method creates a file which is the shopping list'''
        with open(list_name+'.txt','a') as sl:
            sl.write(description)
            sl.write('\n')
        #as a list is created, a file keeping track of names of shoppping lists
        with open('shoplogger.txt','a') as f:
            f.write(list_name)
            f.write('\n')

    def share_container(self,file_name):
        '''This method maintains  a file which logs all shared shopping lists'''

        with open('shared_lists.txt','a') as f:
            f.write(file_name)
            f.write('\n')

    def show(self):
        '''show function reads and returns the records in a file'''
        slist=[]
        with open('shopping_list.txt','r') as sl:
            #just return a list
            for records in sl:


                slist.append(records)

        return slist



