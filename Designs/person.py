class Person:
    def register(self,username,emailaddress,password):
        with open('user.txt', 'w') as f:
            f.write(username)
            f.write(emailaddress)
            f.write(password)
        

    def validator(self):
        with open('user.txt','r') as f:
            return f
        