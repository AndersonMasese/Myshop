class ShareList:
    '''class contains lists which are shared'''
    shared_shopping_list_container = []
    shareditemsdictionary={}

    def shared_shopping_list_container(self):
        return self.shared_shopping_list_container

    def shareditemsdictionary(self):
        return self.shareditemsdictionary

    def add_shared_shopping_list(self,listname):
        self.shared_shopping_list_container.append(listname)
        return shared_shopping_list_container

