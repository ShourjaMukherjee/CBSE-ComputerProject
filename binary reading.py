import pickle

class Account():                                                                                #every user will have an object of this class
    def __init__(self, FirstName, LastName, DOB, Password, Username ):
        self.FirstName = FirstName
        self.LastName = LastName
        self.DOB = DOB
        self.Password= Password
        self.Username =  Username
        self.Highscore = 0

    def display(self):
        print ("Username: ", self.Username)
        print ("Password: ", self.Password)
        print ("Highscore: ", self.Highscore)
file=open('Accounts.dat','rb')
if not file:
    print ('error')
else:
    while True:
        try:
            x=pickle.load(file)
            x.display()
        except EOFError:
            print ('That is all')
            break
file.close()
