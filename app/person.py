'''This module contains class person which declares the basic attributes of user '''


class Person:
    account = []

    def register(self, username, emailaddress, password, *args):
        '''method for registering people into the common list'''
        if type(username)!=str:
            return 'only strings allowed for names'
        else:
            self.account.append(username)
            self.account.append(emailaddress)
            self.account.append(password)
            return self.account

    def login(self):
        '''validate login credentials'''
        return self.account
