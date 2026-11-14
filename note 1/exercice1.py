#Convert the string "250" into an integer and add 50 to it.
#Convert the integer 100 into a string and concatenate it with " EUR".
#Convert 99.99 into an integer and explain the result.
#Check whether a string containing only spaces has a meaningful value.
#Try converting "hello" into an integer and observe the error.

#variables
string = "250"
integer = 100
float = 99.99
second_string = "   "
third_string = "hello"
forth_string = " EUR"


#fonctionality
string_toInt = int(string)
string_toInt += 50
print(string_toInt)

integer_tostring = str(integer)
total = integer_tostring + forth_string
integer_tostring += " EUR"
print(total)
print(integer_tostring)

float_toInt = int(float)
print(f"the float {float}, has been converted to an interger = {float_toInt}")

check_second_string = bool(second_string.strip())
if check_second_string:
    print("second string contains meaningful value")
else:
    print("second string has no meaningful value")


third_string_toInt = int(third_string)
print(third_string_toInt)


