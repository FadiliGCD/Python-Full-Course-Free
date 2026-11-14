
#lenght of a string
string = "my name is fadili"
string_lengh = len(string)
print(string_lengh)

#find method  #returns potion of the charachter you want to fing in a string in first occurance #it starts from 0
find_a = string.find("a")
print(find_a)
#for last accurance we use .rfind()
find_a_r = string.rfind("a")
print(find_a_r)

#capitlize, upper and lowe methods 
string_capitlized = string.capitalize()
print(string_capitlized) #this capitlizes the first character of the string
string_upper = string.upper()
print(string_upper)     #this turns the whole string uppercase
string_lower = string.lower()
print(string_lower)    #this returns the whole string lowercase

#isdigit method / it returns true id the string is all digits otherwise false
string_isdigits = string.isdigit()
print(string_isdigits)

#isalpha method / it retruns true is the string is all alphabitical charchters #note is it contains white space it will return false
string_isalpha = string.isalpha()
print(string_isalpha)

#count method  / it counts the amount of charachter you want in a string
string_count = string.count("a")
print(string_count)  # the output is 2 because we have 2 a's in string variable

#replace method / it replaces a charachter with another charchter inside the string
string_replace = string.replace(" ", "")
print(string_replace)  #here we replaced white space " " with no space ""