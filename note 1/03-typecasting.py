#type casting is converting a variable from a data type to another data type

name = "fadili"
name2 = ""
age = 24
hight = 1.83
isStudnt = True

# type(name) this action shows the data type of the variable
print(type(name))
print(f"the data type of {age} is {type(age)}")

#typecasting: we use int() float() str() bool()
print(f"hight is: {type(hight)}")
hight = int(hight)
print(f"now hight is {type(hight)}")
#lets see the example of bool and str
#name now is string if we covert it to bool it will output true if name variable has a value, if not it will show false.
#this is usefull to check wether the user entered a value or not
check_name = bool(name)
check_name2 = bool(name2)
print(f"does name has a value? {check_name}")
if name:
    print("yes")
else:
    print("no")
print(f"does name2 has a value? {check_name2}")
if name2:
    print("yes")
else:
    print("no")