# This is an application
users=[] 
class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        
class credentials: 
    def __init__(self, site ,username, password):
        self.site=site
        self.username=username
        self.password=password

class Main:
    
    def register():
        print("Create new account")
        username=input("Enter username: ")
        password=input("Enter new password: ")
        c_password=input("Confirm your password: ")
        if password==c_password:
            user=User(username,password)
            users.append(user)
            Main.login()

        else:
            print("passwords do not match")
            Main.register() 
            
    def login():
        print("Login to your account")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for x in users:
            if x.username==username and x.password==password:
                print("Login successful")
            else:
                print("Invalid login attempt")
                Main.login()

            

    def navigate (x):
        if x=="1":
            Main.register()
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
Main.navigate(option)