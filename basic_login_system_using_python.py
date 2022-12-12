#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def register():
    db=open("database.txt","r")
    import re
    email_id_pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    email_id=input("Enter your email id: ")
    from getpass import getpass
    password1=getpass("Enter password: ")
    password2=getpass("Confirm password: ")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))
    #email_id_validation
    if not re.search(email_id_pattern,email_id):
        print(f"{email_id} is InValid. Please try again")
        register()
    #password_validation
    elif password1!=password2:
        print("Enter password and Confirm password is Not same,Try Again")
        register()
    elif (len(password2)<5):
        print("Not valid!, password must be 5 to 16 characters")
        register()
    elif not re.search('[A-Z]',password2):
        print("Not valid!, password must contain atleast one capital letter")
        register()
    elif not re.search('[a-z]',password2):
        print("Not valid!, password must contain atleast one lowercase letter")
        register()
    elif not re.search('[0-9]',password2):
        print("Not valid!, password must contain atleast one digit")
        register()
    elif re.search('\s',password2):
        print("Not valid!, password should not contain white space")
        register()
    elif not re.search('[!@#%&*_+=$]',password2):
        print("Not valid!, password must contain atleast one symbol(!@#%&*_+=$)")
        register()
    elif email_id in d:
        print("User already exists")
        register()
    else:
        db=open("database.txt","a")
        db.write(email_id+", "+password2+"\n")
        print("You have been registered successfully!")
        
def access():
    db=open("database.txt","r")
    email_id=input("Enter your email id: ")
    from getpass import getpass
    password1=getpass("Enter password: ")
    if not len(email_id or password1)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
        
        try:
            if data[email_id]:
                try:
                    if password1==data[email_id]:
                        print("Login success")
                    else:
                        print("Password or Email incorrect")
                except:
                    print("Incorrect password or Email id")
            else:
                print("Email id doesn't exist")
        except:
            print("Login error")
            
def forgot_password():
    db=open("database.txt","r")
    email_id=input("Enter your email id: ")
    if not len(email_id)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
        
        try:
            if data[email_id]:
                try:
                    if email_id in data:
                        print("your password is ",data[email_id])
                    else:
                        print("Entered mail id is incorrect")
                except:
                    print("Incorrect mail id")
            else:
                print("Mail id doesn't exist")
        except:
            print("Error, Try again")          
def home(option=None):
    
    option=input("Welcome, Login system using python\n"+"Choose the option(Case sensitive) and type in: Login | Signup | Forget password: ")
    if option=="Login":
        access()
    elif option=="Signup":
        register()
    elif option=="Forget password":
        forgot_password()
    else:
        print("Please enter an option")
home()
            

            



# In[ ]:




