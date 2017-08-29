class Person:
    def register(self,username,emailaddress,password):
        with open('user.txt', 'a') as f:
            f.write(username)
            f.write('\n')
            f.write(emailaddress)
            f.write('\n')
            f.write(password)
            f.write('\n')
        

    def validator(self):
        file_contents=[]
        with open('user.txt','r') as f:
            for lines in f:
                #file_contents.append(lines)
                #return file_contents
                return lines
            
