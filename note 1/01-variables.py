# comment.

#to run the program, use python filename.py in terminal

#display fonction: print("") or print('')
print("test 2")

#variables:
#------------------------string-------------------
name = "fadili"
name2 = 'fadilox'
print("my name is", name) #not so clean code
print(f"my name is {name}") #using 'f' format (f string) is better. Clean code
#-----------------------integer------------------
number1 = 6
number2 = 4
print(f"{number1}+{number2}={number1+number2}")
#-----------------------float-------------------
number3 = 3.567
#-----------------------boolean----------------
isWorking = True
isStudent = False
if isStudent:
    print(f"{name} is a student")
else:
    print(f"{name} is not a student")
