#user input validation system!
import re
import sys

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

#welcome messgage
print("Welcome to the user input validation system")

#name validation
while True:
    user_name = input("Enter a username: ")

    #check is there is space in user name
    if len(user_name) < 3 :
        print("A valid user name must contain 3 letter at least!\nTry again") 
        

    #check is any numbers exist in the user name
    elif not user_name.isalpha() :
        print("A user name must be all letters!\nTry again")
    

    #check is there is space in user name         
    elif " " in user_name:
        print("A user name can't contain white space\nTry again")              
        
    else:
        break

#check age
while True:
    age = input("Enter your age: ")
    if any(char.isalpha() for char in age):
        print("Please enter a valide age!\nTry again")
    elif " " in age:
        print("Please enter a valide age!\nTry again")
    else:
        age = int(age)
        #age is a valid interger now, before it was accepted as string
        if age<18:
            print("You have to be 18 to register") 
            sys.exit()
        elif age>100:
            print("You are too old to register")
            sys.exit()
        else:
            break

#check email
while True:
    email = input("add your email: ")
    if "@" not in email:
        print("your email is not valid!\nTry again")
    elif "." not in email:
        print("your email is not valid!\nTry again")
    elif email.count("@") >= 2:
        print("your email is not valid!\nTry again")
    

    else:
        break

#check password
while True:
    password = input("Enter password \nit must be at 8 charchters long\nat least 1 capitle letter\nat least one special charachter\nPassword: ")
    if len(password) < 8 :
        print("password must be at least 8 charachters long!\nTry again")
    elif any(word.isupper() for word in password) == False:
        print("password must have at least one upper case letter")
    elif  regex.search(password) == None:
        print("password must contain special charcters!\nTry again")
    elif any(number.isdigit() for number in password) == False:
        print("password must contain at least one number")
    else:
        break

#password remembrance chaeck
while True:
    password2 = input("re-enter password: ")
    if password2 != password:
        print("passsword doesnt match try again: ")
    else:
        break

#output
print("------------REGISTRATION SUCCESSFUL-------------\n" \
f"username: {user_name}\n"
f"age: {age}\n"
f"email: {email}\n"
"-----------------account succesfully created-----------------------")


