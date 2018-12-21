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

#s = Account("a","a","","a","a")

file = open ("Accounts.dat","rb")

if (not file):

    print ("Unable to open file")
    
else:

    print ("Displaying Contents of file record by record:- ")
    while True:
        
        try:
            s=pickle.load(file)
            s.display()
            print ()

        except EOFError:
            break

    file.close

    
