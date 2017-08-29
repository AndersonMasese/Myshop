from person import Person

class ShoppingList:
    
    def create(self,list_name,description):
        with open('shopping_list.txt','a') as sl:
            sl.write(list_name+'  ' +'  '+description)
            sl.write('\n')
    def show(self):
        slist=[]
        with open('shopping_list.txt','r') as sl:
            #just return a list
            for records in sl:


                slist.append(records)

        return slist



