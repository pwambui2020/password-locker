# This is an application 

class Main:
    def register():
        print("Create new account")
        username = input ("Enter username: ")
        password = input (" Enter new password: ")
        c_password = input (" Confirm your password: ")
        if password  == c_password:
            print ("passwords match")
        else:
            print:("passwords do not match")


    def navigate (x):
        if x=="1":
            Main.Register()
        elif x=="2":
            print("Login")
        elif x=="3":
            exit()
        else:
            print ("invalid password")


    
print ("Welcome to Password Locker")
print ("Select an option to continue")
print ("1.Register\n2.Login\n3.Exit") 
option=input()
