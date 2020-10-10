# This is an application 

#  class main:

def navigate (x):
    if x=="1":
      main.Register()
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
