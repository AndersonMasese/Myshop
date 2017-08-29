from person import Person

class ShoppingList:
    
    def create(self,list_name,description):
        '''This function creates a file which is the shopping list'''
        with open(list_name+'.txt','a') as sl:
            sl.write(description)
            sl.write('\n')
    def show(self):
        '''show function reads and returns the records in a file'''
        slist=[]
        with open('shopping_list.txt','r') as sl:
            #just return a list
            for records in sl:


                slist.append(records)

        return slist



