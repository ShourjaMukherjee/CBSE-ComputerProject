import tkinter as tk
from tkinter import ttk
import pickle
import os
import pygame
import subprocess, sys 
##Accounts_File = open("Accounts.dat", "ab+")
#List_of_Usernames = ["AA"]
#with open('Username.dat', 'wb') as f:
#   pickle.dump(List_of_Usernames,f)


#~~~~~~~~~~~~~~~~~~~~~~ACCOUNT CLASS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Account():                                                                                #every user will have an object of this class
    def __init__(self, FirstName, LastName, DOB, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.DOB = DOB
        self.Password= Password
        self.Username =  self.FirstName[0] + self.LastName[0] + self.DOB[0] + self.DOB[1] + self.DOB[3] + self.DOB[4] + self.DOB[8] + self.DOB[9]
        self.Highscore=0
		
    def display(self):
        print ("Username: ", self.Username)
        print ("Password: ", self.Password)

        
            

A=Account("A","A","00/00/0000","A")
##with open('LoggedInAccount.dat', 'wb') as f:
##    pickle.dump(A,f)        
#LARGE_FONT= ("Verdana", 25)
LARGE_FONT= ("Courier", 16, "bold", "underline")
SMALL_FONT= ("Courier", 8)

#~~~~~~~~~~~~~~~~~~~~~APPLICATION INITIALIZATION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class  ArcadeSystem(tk.Tk):                                                                     # initializing the app
    def __init__(self, *args, **kwargs):                                                                                            #I DON'T KNOW WHAT TO COMMENT ON THIS CLASS. 

        tk.Tk.__init__(self, *args,**kwargs)

        #tk.Tk.iconbitmap(self, default="arcadeicon.ico")                                           # This is the app icon. since the fifa 14 icon was already there on the macbook, I used it. So the line is commented because you don't have the icon.
        tk.Tk.wm_title(self, "Arcade Gaming Station")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)          #placement of the frame
        container.grid_rowconfigure(0, weight=1)                    #uhhh
        container.grid_columnconfigure(0, weight=1)                 #uhhh

        self.frames = {}

        for F in (StartPage, Page1, LoginPage, NewAccPage, PlayPage, AreYouSure, EditPage, EditUsername, EUsedName, UsernameChanged, EditPassword, PasswordChanged, NoMatch, AccSuccessful, AccFailed, UsedName, InvalidDOB, LoginFailed, LoginSuccess): 

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#~~~~~~~~~~~~~~~~~~~~~~START PAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StartPage(tk.Frame):                                                                      # This is starting Frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)                                                         #parent is calling parent class, that is ArcadeSystem
        
        self["bg"] = "light blue"
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label^ in the frame

                                
        Play_Button = tk.Button(self, text="PLAY", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                             # A button that is used to move to the next frame
                            command=lambda: controller.show_frame(Page1))
        Play_Button.pack()                                                                      # Placing Play button^ in the frame

        Exit_Button = tk.Button(self, text="Exit Application", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                              # Button to close the app
                            command=self.close_window)
        Exit_Button.pack()                                                                      # Placing Exit Button^ in the frame

    def close_window(self):
        app.destroy()

#~~~~~~~~~~~~~~~~~~~~~PAGE TO CHOOSE WHETHER YOU LOGIN OR MAKE A NEW ACCOUNT~~~~~~~~~~~~~        

class Page1(tk.Frame):                                                                          # Frame that is raised when 'Play Button' is hit

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)                                                         #parent is calling parent class, that is ArcadeSystem
        self["bg"] = "light blue"
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label in the frame

        Login_Button = tk.Button(self, text="Log In", font=SMALL_FONT,  bg="green", fg="white", activeforeground="black",                                        # Button to raise Login Frame
                            command=lambda: controller.show_frame(LoginPage))                           
        Login_Button.pack()                                                                     # Placing Login button^ in the frame
        
        NewAcc_Button = tk.Button(self, text="Make Account", font=SMALL_FONT, bg="blue", fg="white", activeforeground="black",                                 # Button to raise New Account frame
                            command=lambda: controller.show_frame(NewAccPage))
        NewAcc_Button.pack()                                                                    # Placing New Account button^ in the frame
        
        Main_Button = tk.Button(self, text="Back to Home", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                   # Button to raise Starting Frame
                            command=lambda: controller.show_frame(StartPage))
        Main_Button.pack()                                                                      # Placing Back to Home^ in the Frame


#~~~~~~~~~~~~~~~~~~~~LOGIN PAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LoginPage(tk.Frame):                                                                      # Frame that is raised when 'Login button' is hit                        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)                                                         #parent is calling parent class, that is ArcadeSystem

        global LUsername_Entry                                                                  # calling the global variables
        global LPassword_Entry                                                                  # calling the global variables

        self['bg']="light blue"
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT,  bg="indigo", fg="white")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label^ in the frame

        LUsername = tk.Label(self, text="Username", font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=50)                            # Creating and placing a label "Username"
        LUsername_Entry = tk.Entry(self)                                                        # Creating an Entry box for user to enter username
        LUsername_Entry.place(x=100,y=50)                                                       # Placing the Entry box for user to enter username

        LPassword = tk.Label(self, text="Password", font=SMALL_FONT, bg="light blue", fg="indigo",).place(x=20,y=75)                            # Creating and placing a label "Password"
        LPassword_Entry = tk.Entry(self, show="*")                                              # Creating an Entry box for user to enter password
        LPassword_Entry.place(x=100,y=75)                                                       # Placing the Entry box for user to enter password

        #space for buttons

        LogIn_Button = tk.Button(self, text="LOGIN", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                           # Button that calls check(self) member function
                            command=self.check)
        LogIn_Button.place(x=75,y=100)                                                         # Placing the Button^        


        Main_Button = tk.Button(self, text="Back to Home", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                    # Button to raise Starting Frame
                            command=self.MainPage)
        Main_Button.place(x=75,y=125)                                                          # Placing the button^




    def MainPage(self):
        LPassword_Entry.delete(0, tk.END)
        LUsername_Entry.delete(0, tk.END)

        app.show_frame(StartPage)


    def check(self):
        #global L
        flag=True
        Account_File = open("Accounts.dat", "rb+")                                          # A file 'Accounts.dat' is opened in 'read and write as binary' mode with the identifier Username_File 
        while flag==True:                                                                             # infinite loop to check for errors
            try:
                #print ("Entered Username: ", LUsername_Entry.get())
                #print ("Entered Password: ", LPassword_Entry.get())
                A = pickle.load(Account_File)                                                   # A record from the file is loaded. In this case, an object of class Account
                #A.display()
                #print ()
                if LUsername_Entry.get() == A.Username:
                    #print (" Username Checked")
                    #print ()
                    if LPassword_Entry.get() == A.Password:
                        #print ("Password Checked")
                        #print ()
                        f=open('LoggedInUser.txt','w')
                        f.write(A.FirstName)
                        f.write("\n")
                        f.write(A.Username)
                        f.write("\n")
                        f.write(A.LastName)
                        f.write("\n")
                        f.write(A.DOB)
                        f.write("\n")
                        f.write(A.Password)
                        f.close()

                        file=open('LoggedInAccount.dat','wb')
                        pickle.dump(A,file)
                        file.close()
                            
                        Account_File.seek(0,0)
                        flag=False
                        app.show_frame(LoginSuccess)                                            # if condition^ is satisfied, LoginSuccess Frame is raised
                        LPassword_Entry.delete(0, tk.END)
                        LUsername_Entry.delete(0, tk.END)
                    else:
                        #print ("Secondary else")
                        flag=False
                        app.show_frame(LoginFailed)                                             # if condition^ is satisfied, LoginFailed Frame is raised
                else:
                    pass                                                                        # moves to next account if usernames do not match.  
                        
            except EOFError:                                                                                
                flag=False
                #print ("Primary else")
                app.show_frame(LoginFailed)                                                    # if no username match is found, LoginFailed Frame is raised
        

        

#~~~~~~~~~~~~~~~~~~~~~NEW ACCOUNT PAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NewAccPage(tk.Frame):                                                                     #Frame that is raised when "New Account" Button is hit
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white", activeforeground="black")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label^ in the frame

        global Password_Entry                                                                   # calling the global variables
        global RePassword_Entry                                                                 # calling the global variables
        global FirstName_Entry                                                                  # calling the global variables
        global LastName_Entry                                                                   # calling the global variables
        global DOB_Entry                                                                        # calling the global variables
        global Username_Entry                                                                   # calling the global variables

        FirstName = tk.Label(self, text="First Name: ",font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=50)                        # Creating and placing a label "First Name: "                        
        FirstName_Entry = tk.Entry(self)                                                        # Creating an Entry box for user to enter First Name
        FirstName_Entry.place(x=150,y=50)                                                       # Placing the Entry box^

        LastName = tk.Label(self, text="Last Name: ",font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=75)                          # Creating and placing a label "Last Name: "
        LastName_Entry = tk.Entry(self)                                                         # Creating an Entry box for user to enter Last Name
        LastName_Entry.place(x=150,y=75)

        DOBLabel = tk.Label(self, text="DOB(DD/MM/YYYY): ",font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=100)                   # Creating and placing a label "DOB: "
        DOB_Entry = tk.Entry(self)                                                              # Creating an Entry box for user to enter DOB
        DOB_Entry.place(x=150,y=100)

        Username = tk.Label(self, text="Username: ", font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=125)                          # Creating and placing a label "Username: "
        Username_Entry = tk.Entry(self)                                                         # Creating an Entry box for user to enter Username
        Username_Entry.place(x=150,y=125)

        Password = tk.Label(self, text="Password: ", font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=150)                          # Creating and placing a label "Password: "
        Password_Entry = tk.Entry(self, show="*")                                               # Creating an Entry box for user to enter password. Text entered appears to users as "*"
        Password_Entry.place(x=150,y=150)

        RePassword = tk.Label(self, text="Re-enter Password: ", font=SMALL_FONT, bg="light blue", fg="indigo").place(x=20,y=175)               # Creating and placing a label "Re-enter Password: "
        RePassword_Entry = tk.Entry(self, show="*")                                             # Creating an Entry box for user to re-enter password. Text entered appears to users as "*"
        RePassword_Entry.place(x=150,y=175)

        

        #~~~~~~~~~~~~~Buttons~~~~~~

        Create_Button = tk.Button(self, text="Create Account", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                # Button that calls Check(self) member function
                                   command=self.Check)
        Create_Button.place(x=100,y=200)                                                        # Placing the button^
        
        Main_Button = tk.Button(self, text="Back to Home", font=SMALL_FONT,  bg="red", fg="white", activeforeground="black",                                # Button to raise Starting Frame
                            command=self.MainPage)
        Main_Button.place(x=100,y=300)                                                          # Placing the button^




    def MainPage(self):
        FirstName_Entry.delete(0, tk.END)
        LastName_Entry.delete(0, tk.END)
        DOB_Entry.delete(0, tk.END)
        Password_Entry.delete(0, tk.END)
        RePassword_Entry.delete(0, tk.END)
        Username_Entry.delete(0, tk.END)

        app.show_frame(StartPage)



    def Check(self):                                                                            # member function of NewAccPage class that checks legitability of credentials entered
        flag = checkDOB(DOB_Entry.get())                                                        # Calls checkDOB() to check if date entered is valid
        if flag == False:                                                                       # False means DOB entered is invalind. This is a Condition
            app.show_frame(InvalidDOB)                                                          # if above^ condition is satisfied, InvalidDOB frame is raised
        else:                                                                                   # True means DOB entered is valid. This is a condition
            Username_File = open("Username.dat", "rb+")                                         # A file 'Username.dat' is opened in 'read and write as binary' mode with the identifier Username_File
            while True:                                                                         # infinite loop to check for errors
                try:
                    List_of_Usernames = pickle.load(Username_File)                              # A record from the file is loaded. In this case, it's a list of all Usernames and the record of type list is referenced to identifier 'List_of_Usernames'
                except EOFError:                                                                                
                    break                                                                       # if the file reaches its end, it exits the loop
            if Username_Entry.get() in List_of_Usernames:                                       # checks if the username entered by user is taken or not.
                app.show_frame(UsedName)                                                        # if condition^ is satisfied, UsedName Frame is raised
            else:                                                                               # if the username entered is valid, the following ocuurs:- 
                if Password_Entry.get() == RePassword_Entry.get():                              # condtion to see if password and re-entered password is identical
                    A.FirstName = FirstName_Entry.get()                                         # assigns value of First Name entered to the corresponding attribute of object of class Account
                    A.LastName = LastName_Entry.get()                                           # assigns value of Last Name entered to the corresponding attribute of object of class Account
                    A.DOB = DOB_Entry.get()                                                     # assigns value of DOB entered to the corresponding attribute of object of class Account
                    A.Password = Password_Entry.get()                                           # assigns value of Password entered to the corresponding attribute of object of class Account
                    A.Username =  Username_Entry.get()                                          # assigns value of Username entered to the corresponding attribute of object of class Account
                    
                    List_of_Usernames.append(A.Username)                                        # Username of new account created is appended to the list containing all of the usernames

                    Username_File.seek(0,0)                                                     # places the pointer to the beginning of the file 'Username.dat'
                    pickle.dump(List_of_Usernames, Username_File)                               # dumps the appended list to the file 'Username.dat'
                    Username_File.close()                                                       # close the file ^

                    with open('Accounts.dat', 'ab') as f:                                       # have the file 'Accounts.dat' open in append binary mode as 'f'
                        pickle.dump(A,f)                                                        # dump the newly created account(in the form of object of class Account) into 'f'

                    FirstName_Entry.delete(0, tk.END)
                    LastName_Entry.delete(0, tk.END)
                    DOB_Entry.delete(0, tk.END)
                    Password_Entry.delete(0, tk.END)
                    RePassword_Entry.delete(0, tk.END)
                    Username_Entry.delete(0, tk.END)
                    
                    app.show_frame( AccSuccessful)                                              # raises the AccSuccessful frame

                else:                                                                           # if the passwords do not match:-
                    app.show_frame( AccFailed)                                                  # raises the AccFailed frame





class PlayPage(tk.Frame):                                                                          # Frame that is raised when 'Play Button' is hit

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)                                                         #parent is calling parent class, that is ArcadeSystem

        self['bg']='light blue'
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT,  bg="indigo", fg="white", activeforeground="black")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label in the frame


##        file = open("LoggedInAccount.dat", "rb")
##        while True:
##            try:
##                U=pickle.load(file)
##                U.display()
##            except EOFError:
##                break
##            
##        Flabel = tk.Label(self, text=U.FirstName)
##        Flabel.pack()
##
##        Ulabel = tk.Label(self, text=U.Username)
##        Ulabel.pack()

        TicTacToe_Button = tk.Button(self, text="Tic Tac Toe", font=SMALL_FONT, bg="yellow", fg="black", activeforeground="black",                                        # Button to raise Login Frame
                            command= self.opentictactoe)
        #lambda: exec(open("tictactoe11.exe").read()
        TicTacToe_Button.pack()                                                                     # Placing Login button^ in the frame
        
        Platform_Button = tk.Button(self, text="JUMP STREET(Platformer)", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                 # Button to raise New Account frame
                            command=self.openplatform)
        Platform_Button.pack()                                                                    # Placing New Account button^ in the frame
        

        Edit_Button = tk.Button(self, text="Edit Account", font=SMALL_FONT, bg="orange", fg="white", activeforeground="black",                                   # Button to raise Edit account Frame
                            command=lambda: controller.show_frame(EditPage))
        Edit_Button.pack()   

        View_Button = tk.Button(self, text = "View Account Details. ", font=SMALL_FONT, bg="pink", fg="black", activeforeground="black",
                                command=ViewDetails)
        View_Button.pack()

        Delete_Button = tk.Button(self, text="Delete Account", font=SMALL_FONT,  bg="crimson", fg="white", activeforeground="black",                                   # Button to raise Starting Frame
                            command=lambda: controller.show_frame(AreYouSure))
        Delete_Button.pack() 
        
        Main_Button = tk.Button(self, text="Log Out", font=SMALL_FONT, bg="dark blue", fg="white", activeforeground="black",                                   # Button to raise Starting Frame
                            command=self.LogOut)
        Main_Button.pack()                                                                      # Placing Back to Home^ in the Frame


    def opentictactoe(self):
	

        opener ="open" if sys.platform == "darwin" else "xdg-open"	
        subprocess.call([opener, "./tictactoe.py"])                                                #for linux
	
        #os.startfile("tictactoe.py")                 #-- os module is for windows
		
    def openplatform(self):
        opener ="open" if sys.platform == "darwin" else "xdg-open"	
        subprocess.call([opener, "./main.py"])                                                #for linux
	
        #os.startfile("main.py")
        
    def LogOut(self):
       	os.remove("LoggedInAccount.dat")
        os.remove("LoggedInUser.txt")
        app.show_frame(StartPage)



class AreYouSure(tk.Frame):                                                                          # Frame that is raised when 'Play Button' is hit

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)                                                         #parent is calling parent class, that is ArcadeSystem

        self['bg']='light blue'
        
        label = tk.Label(self, text="Are you sure you want to Delete Account?", bg="light blue", fg="black", activeforeground="black", font=SMALL_FONT)                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label in the frame

        Yes_Button = tk.Button(self, text="Yes", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                    # Button to raise Starting Frame
                            command=self.DeleteAccount)
        Yes_Button.pack() 
        
        No_Button = tk.Button(self, text="No", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                    # Button to raise Starting Frame
                            command=lambda: controller.show_frame(PlayPage))
        No_Button.pack()                                                                      # Placing Back to Home^ in the Frame

    

        
    def DeleteAccount(self):
        Username_File = open("LoggedInAccount.dat", "rb")
        while True:
            try:
                U=pickle.load(Username_File)
                    #U.display()
            except EOFError:
                break
            #U.Username = EUsername_Entry.get()
        
#        Username_File.close()

        file1 = open ("Accounts.dat","rb+")
        file2 = open ("xyz.dat","wb")
        L=[]
        a=U.Username
                
        if (not file1):
            print ("Unable to create file.")
        elif (not file2):
            print ("Unable to create file.")
        else:
            while True:
                try:
                    s=pickle.load(file1)
                    if (s.Username!=a):
                        pickle.dump(s,file2)
                    else:
                        continue
                        
                except EOFError:
                    break
        s=0
        file1.close()
        file2.close()
        
        os.remove('Accounts.dat')
        os.rename('xyz.dat','Accounts.dat')

        file2 = open ("xyz.dat","wb")

        a=U.Username
        if (not Username_File):
            print ("Unable to create file.")
        elif (not file2):
            print ("Unable to create file.")
        else:
            while True:
                try:
                    s=pickle.load(Username_File)
                    for i in range(len(s)):
                        if s[i]==a:
                            pass
                        else:
                            L.append(s[i])

                except EOFError:
                    break
        pickle.dump(L,file2)
        Username_File.close()
        file2.close()

        os.remove('Username.dat')
        os.rename('xyz.dat','Username.dat')

        self.LogOut()

    def LogOut(self):
        os.remove("LoggedInAccount.dat")
        os.remove("LoggedInUser.txt")
        app.show_frame(StartPage)


class EditPage(tk.Frame):                                                                     #Frame that is raised when "Edit Account" Button is hit
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white", activeforeground="black")                           # Creating a label "ARCADE SYSTEM"
        label.pack(pady=10,padx=10) #or use grid                                                Placing the label^ in the frame

        EditU_Button = tk.Button(self, text="Edit Username", font=SMALL_FONT, bg="blue", fg="white", activeforeground="black",                                    
                          command=lambda: controller.show_frame(EditUsername))
        EditU_Button.pack()                                                                     

        EditP_Button = tk.Button(self, text="Edit Password", font=SMALL_FONT, bg="yellow", fg="black", activeforeground="black",                                    
                            command=lambda: controller.show_frame(EditPassword))
        EditP_Button.pack()

        GoBack_Button = tk.Button(self, text="GoBack", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                         
                            command=lambda: controller.show_frame(PlayPage))
        GoBack_Button.pack()                                                        




class EditUsername(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white", activeforeground="black")
        label.pack(padx=10, pady=10)

        label1 = tk.Label(self, text="Enter New Username", bg="light blue", fg="indigo", activeforeground="black")
        label1.pack()

        global EUsername_Entry
        
        EUsername_Entry = tk.Entry(self)
        EUsername_Entry.pack()

        EUsername_Button = tk.Button(self, text="Submit New Username", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",
                                      command=self.EUCheck)
        EUsername_Button.pack()

        GoBack_Button = tk.Button(self, text="GoBack", font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                     
                            command=lambda: controller.show_frame(PlayPage))
        GoBack_Button.pack()                                                        

        

    def EUCheck(self):
        global EUsername_Entry
        Username_File = open("Username.dat", "rb+")                                         # A file 'Username.dat' is opened in 'read and write as binary' mode with the identifier Username_File
        while True:                                                                         # infinite loop to check for errors
            try:
                List_of_Usernames = pickle.load(Username_File)                              # A record from the file is loaded. In this case, it's a list of all Usernames and the record of type list is referenced to identifier 'List_of_Usernames'
                #print (List_of_Usernames)
            except EOFError:                                                                                
                break
            
        if EUsername_Entry.get() in List_of_Usernames:
            #print ("False")
            #print (EUsername_Entry.get())
            app.show_frame(EUsedName)
        else:
            #print ("True")
            #print (EUsername_Entry.get())
            file = open("LoggedInAccount.dat", "rb")
            while True:
                try:
                    U=pickle.load(file)
                    #U.display()
                except EOFError:
                    break
            #U.Username = EUsername_Entry.get()
            file.close()
#            Username_File.close()

            file1 = open ("Accounts.dat","rb+")
            file2 = open ("xyz.dat","wb")
            L=[]
            a=U.Username
                
            if (not file1):
                print ("Unable to create file.")
            elif (not file2):
                print ("Unable to create file.")
            else:
                while True:
                    try:
                        s=pickle.load(file1)
                        if (s.Username!=a):
                            pickle.dump(s,file2)
                        else:
                            continue
                        
                    except EOFError:
                        break
            file1.close()
            file2.close()

            #Username_File.close()
            #file1 = open ("Username.dat","rb+")
            file2 = open ("xyz.dat","wb")

            a=U.Username
            if (not Username_File):
                print ("Unable to create file.")
            elif (not file2):
                print ("Unable to create file.")
            else:
                while True:
                    try:
                        s=pickle.load(Username_File)
                        for i in range(len(s)):
                            if s[i]==a:
                                pass
                            else:
                                L.append(s[i])
    
                    except EOFError:
                        break
                Username_File.close()
                file2.close()
                U.Username = EUsername_Entry.get()
                L.append(U.Username)
                with open("xyz.dat","wb") as file:
                    pickle.dump(L,file)

                os.remove('Username.dat')
                os.rename('xyz.dat','Username.dat')

                with open("xyz.dat","ab") as file:
                    pickle.dump(U,file)

                os.remove('Accounts.dat')
                os.rename('xyz.dat','Accounts.dat')

                
                
                with open("LoggedInAccount.dat","wb") as file:
                    pickle.dump(U,file)

                f=open('LoggedInUser.txt','w')
                f.write(U.FirstName)
                f.write("\n")
                f.write(U.Username)
                f.write("\n")
                f.write(U.LastName)
                f.write("\n")
                f.write(U.DOB)
                f.write("\n")
                f.write(U.Password)
                f.close()

                EUsername_Entry.delete(0, tk.END)
                
                app.show_frame(UsernameChanged)


class UsernameChanged(tk.Frame):                                                                       # Frame that is raised if the username is already taken
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Username has been changed.", font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                 # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Continue", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                    # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(PlayPage))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button


class EUsedName(tk.Frame):                                                                       # Frame that is raised if the username is already taken
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Username has already been taken.", font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                 # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Try Again", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                    # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(EditUsername))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button



class EditPassword(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        label = tk.Label(self, text="ARCADE SYSTEM", font=LARGE_FONT, bg="indigo", fg="white", activeforeground="black")
        label.pack(padx=10, pady=10)

        label1 = tk.Label(self, text="Enter New Password",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black")
        label1.pack()

        global EPassword_Entry
        
        EPassword_Entry = tk.Entry(self, show="*")
        EPassword_Entry.pack()

        label2 = tk.Label(self, text="ReEnter New Username",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black")
        label2.pack()

        global ReEPassword_Entry
        
        ReEPassword_Entry = tk.Entry(self,show="*")
        ReEPassword_Entry.pack()
        
        EPassword_Button = tk.Button(self, text="Submit New Password", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",
                                      command=self.EPCheck)
        EPassword_Button.pack()

        GoBack_Button = tk.Button(self, text="GoBack",  font=SMALL_FONT, bg="red", fg="white", activeforeground="black",                                   
                            command=lambda: controller.show_frame(PlayPage))
        GoBack_Button.pack()



    def EPCheck(self):
        global EPassword_Entry
        global ReEPassword_Entry

        if EPassword_Entry.get() != ReEPassword_Entry.get():
            app.show_frame(NoMatch)
        else:
            file = open("LoggedInAccount.dat", "rb")
            while True:
                try:
                    U=pickle.load(file)
                    #U.display()
                except EOFError:
                    break
            file.close()

            U.Password = EPassword_Entry.get()

            with open("LoggedInAccount.dat","wb") as file:
                pickle.dump(U,file)

            f=open('LoggedInUser.txt','w')
            f.write(U.FirstName)
            f.write("\n")
            f.write(U.Username)
            f.write("\n")
            f.write(U.LastName)
            f.write("\n")
            f.write(U.DOB)
            f.write("\n")
            f.write(U.Password)
            f.close()

            file1 = open ("Accounts.dat","rb+")
            file2 = open ("xyz.dat","wb")
            L=[]
            a=U.Username
            if (not file1):
                print ("Unable to create file.")
            elif (not file2):
                print ("Unable to create file.")
            else:
                while True:
                    try:
                        s=pickle.load(file1)
                        if (s.Username!=a):
                            pickle.dump(s,file2)
                        else:
                            continue
                        
                    except EOFError:
                        break
            file1.close()
            file2.close()

            with open("xyz.dat","ab") as file:
                pickle.dump(U,file)

            os.remove('Accounts.dat')
            os.rename('xyz.dat','Accounts.dat')

            EPassword_Entry.delete(0, tk.END)
            ReEPassword_Entry.delete(0, tk.END)
            
            app.show_frame(UsernameChanged)
            
                
class PasswordChanged(tk.Frame):                                                                       # Frame that is raised if the username is already taken
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Password has been changed.", font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                 # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Continue", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                    # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(PlayPage))
        NewAcc_Button.place(x=100,y=200) 


class NoMatch(tk.Frame):                                                                      # Frame that is raised if the passwords do not match
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Passwords Do not Match",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black",).pack()                            # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Try Again", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                     # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(EditPassword))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button        
        
#~~~~~~~~~~~~~~~~~~~CONDITIONAL PAGES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class AccSuccessful(tk.Frame):                                                                  # Frame that is raised if the account creation is successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Account Created", font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black",).pack()                                   # Creating and placing label with text "Account Created"
                    

        Login_Button = tk.Button(self, text="Continue", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                      # button that raises the Login page so the user has to log in with his new account
                                command=lambda: controller.show_frame(LoginPage))
        Login_Button.place(x=100,y=200)                                                         # placing the button^






class AccFailed(tk.Frame):                                                                      # Frame that is raised if the passwords do not match
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self['bg']='light blue'
        
        Label = tk.Label(self, text="Passwords Do not Match",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                            # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Try Again", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                    # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(NewAccPage))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button
        




class UsedName(tk.Frame):                                                                       # Frame that is raised if the username is already taken
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Username has already been taken.",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                 # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Try Again", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                     # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(NewAccPage))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button



class InvalidDOB(tk.Frame):                                                                     # Frame that is raised if DOB entered is invalid
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label = tk.Label(self, text="Date Of Birth Entered is invalid.",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                # Creating and placing label displaying appropriate message

        NewAcc_Button = tk.Button(self, text="Try Again", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                     # button that raises the NewAcc frame so that the user can change the incorrect credentails
                            command=lambda: controller.show_frame(NewAccPage))
        NewAcc_Button.place(x=100,y=200)                                                        # placing the button
        

class LoginSuccess(tk.Frame):                                                                   # Frame that is raised if the Login is successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label1 = tk.Label(self, text="You have logged in successfully. ",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black",).pack()                # Creating and placing label with text "Login Successful"
        Label2 = tk.Label(self, text="Welcome ", font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").pack()                                         # Creating and placing label with text "Welcome"
        #Label3 = tk.Label(self, text=A.FirstName).pack()                                        # Creating and placing label with First Name of User
                    

        Continue_Button = tk.Button(self, text="Continue", font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                   # Raises the nest frame, that is PlayPage
                                command=lambda: controller.show_frame(PlayPage))
        Continue_Button.place(x=100,y=200)                                                      # placing the button^


class LoginFailed(tk.Frame):                                                                    # Frame that is raised if the Login Fails
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self['bg']='light blue'
        
        Label1 = tk.Label(self, text="Login Failed",font=SMALL_FONT, bg="light blue", fg="indigo", activeforeground="black").pack()                                     # Creating and placing label with text "Login Failed"
        Label2 = tk.Label(self, text="Username or password entered is incorrect.",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").pack()       # Creating and placing label with appropriate text
                    

        Continue_Button = tk.Button(self, text="Try Again",font=SMALL_FONT, bg="green", fg="white", activeforeground="black",                                 # Returns to Login page so user can retry
                                command=lambda: controller.show_frame(LoginPage))
        Continue_Button.place(x=100,y=200)                                                      # placing the button^


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~VIEW DETIALS WINDOW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ViewDetails():

    global VDWindow

    VDWindow = tk.Tk()

    tk.Tk.wm_title(VDWindow, "Account Details")
    file = open("LoggedInAccount.dat", "rb")
    while True:
        try:
            U=pickle.load(file)
        except EOFError:
            break
    VDWindow['bg']='light blue'
    Flabel = tk.Label(VDWindow, text="First Name: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=25)
    UFlabel = tk.Label(VDWindow ,text=U.FirstName).place(x=175 ,y=25)

    Llabel = tk.Label(VDWindow, text="Last Name: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=50)
    ULlabel = tk.Label(VDWindow ,text=U.LastName).place(x=175 ,y=50)

    Flabel = tk.Label(VDWindow, text="DOB: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=75)
    UFlabel = tk.Label(VDWindow ,text=U.DOB).place(x=175 ,y=75)

    Flabel = tk.Label(VDWindow, text="Username: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=100)
    UFlabel = tk.Label(VDWindow ,text=U.Username).place(x=175 ,y=100)

    Flabel = tk.Label(VDWindow, text="Password: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=125)
    UFlabel = tk.Label(VDWindow ,text=U.Password).place(x=175 ,y=125)

    Flabel = tk.Label(VDWindow, text="Highscore: ",font=SMALL_FONT, bg="light blue", fg="red", activeforeground="black").place(x=75,y=150)
    UFlabel = tk.Label(VDWindow ,text=U.Highscore).place(x=175 ,y=150)

    Exit = tk.Button(VDWindow, text = "Go Back", font=SMALL_FONT, bg="green", fg="white", activeforeground="black", command = close_window3)
    Exit.place(x=100,y=200)
    
    file.close()
    
    VDWindow.geometry("300x300")
    VDWindow.mainloop()

def close_window3():
    global VDWindow
    VDWindow.destroy()
#~~~~~~~~~~~~~~~~~~GAMES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def TicTacToe():
    #print ("TicTacToe")

    global TTTWindow
    
    TTTWindow = tk.Tk()
        
    tk.Tk.wm_title(TTTWindow, "TicTacToe")
    file = open("LoggedInAccount.dat", "rb")
    while True:
        try:
            U=pickle.load(file)
            #U.display()
        except EOFError:
            break

    
    Flabel = tk.Label(TTTWindow, text=U.FirstName)
    Flabel.pack()

    Ulabel = tk.Label(TTTWindow, text=U.Username)
    Ulabel.pack()    

    Exit = ttk.Button(TTTWindow, text = "Exit", command = close_window1)
    Exit.pack()

    file.close()
    
    TTTWindow.geometry("300x300")
    TTTWindow.mainloop()
    

def Platform():
    #print ("Platform")

    global PWindow

    PWindow = tk.Tk()
        
    tk.Tk.wm_title(PWindow, "TicTacToe")
    file = open("LoggedInAccount.dat", "rb")
    while True:
        try:
            U=pickle.load(file)
            #U.display()
        except EOFError:
            break

    Flabel = tk.Label(PWindow, text=U.FirstName)
    Flabel.pack()

    Ulabel = tk.Label(PWindow, text=U.Username)
    Ulabel.pack()    

    Exit = ttk.Button(PWindow, text = "Exit", command = close_window2)
    Exit.pack()

    file.close()

    PWindow.geometry("300x300")
    PWindow.mainloop()

def close_window1():
    global TTTWindow
    TTTWindow.destroy()

def close_window2():
    global PWindow
    PWindow.destroy()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    
def checkDOB(DOB):                                                                              # checks if DOB entered is authentic/eligable
    flag=True                                                                                   # assume that entered DOB is valid
    if len(DOB)!=10:                                                                            # condition to check if DOB is of appropriate length
        flag=False                                                                              # if not, DOB is invalid, Hence False  
    else:                                                                                       # if length is appropriate, further checks are done:-
        d=int(DOB[0]+DOB[1])                                                                    # here d = the date of the day
        m=int(DOB[3]+DOB[4])                                                                    # here m= the month of birth
        y=int(DOB[6]+DOB[7]+DOB[8]+DOB[9])                                                      # here y= the year of birth 
        if m in [1,3,5,7,8,10,12]:                                                              # check to see if m has the values of month corresponding to January, March, May, July, August, October, December
            if d<=31:                                                                           # if yes, then value of d must be lesser than or equal to 31. This is a condition to check so
                flag=True                                                                       # if the condition is satifsied, DOB is valid
            else:
                flag=False                                                                      # if not satisfied, DOB is invalid
        elif m in [4,6,9,11]:                                                                   # else if, a check to see if m has the values of month corresponding to April, June, September, November
            if d<=30:                                                                           # if yes, then value of d must be lesser than or equal to 30. This is a condition to check so
                flag=True                                                                       # if the condition is satifsied, DOB is valid
            else:
                flag=False                                                                      # if not satisfied, DOB is invalid
        elif m==2:                                                                              # else if, a check to see if m has the value correspnding to February
            if y%4==0:                                                                          # if February, check to see if value of y is divsible by 4. (check for leap year)
                if d<=29:                                                                       # if yes, then value of d must be lesser than or equal to 29. This is a condition to check so
                    flag=True                                                                   # if the condition is satifsied, DOB is valid
                else:                                                                           
                    flag=False                                                                  # if not satisfied, DOB is invalid
            elif y%4!=0:                                                                        # if y is not divisible by 4 (NOT leap year), following:-
                if d<=28:                                                                       # if yes, then value of d must be lesser than or equal to 28. This is a condition to check so
                    flag=True                                                                   # if the condition is satifsied, DOB is valid
                else:
                    flag=False                                                                  # if not satisfied, DOB is invalid
        else:                                                                                   # if value of m does not have any of corresponding values of the 12 months, then:-
            flag=False                                                                          # DOB is invalid
    return flag

                
        
    

app = ArcadeSystem()                                                                            # app is the window that the entire program runs on
app.geometry("350x350")                                                                         # sizing of the window
app.mainloop()
