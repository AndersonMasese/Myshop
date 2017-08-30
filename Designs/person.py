class Person:
    '''
    Class is controller of all login and registration activities
    '''
    def register(self,username,emailaddress,password):
        '''method inserts the individual's details into a file'''
        with open('user.txt', 'a') as f:
            f.write(username)
            f.write('\n')
            f.write(emailaddress)
            f.write('\n')
            f.write(password)
            f.write('\n')
        

    def validator(self):
        '''method opens file and returns the individual user contents'''
        file_contents=[]
        with open('user.txt','r') as f:
            for lines in f:
                #file_contents.append(lines)
                #return file_contents
                return lines
            
