import math

#welcome message
print("------------------------------------------------------------------")
print("Welcome the Calculatore programm")

#promt
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
equation = input("Enter the mathimatical equation you want to perform on the two numbers.\n" \
"type + for addition,\n - for substraction,\n / for division,\n * for multyplication,\n ** to user the power,\n sqrt to you the squar root,\n R for remainder of number 1 devided by number 2 \n")

#calculation
result = None
if equation=="+":
    result = a + b
elif equation=="-":
    result = a -b
elif equation=="/":
    if b==0:
        print("Can't devide by 0")
    else:
        result = a/b
elif equation=="*":
    result = a*b
elif equation=="**":
    result = math.pow(a,b)
elif equation=="sqrt":
    sqrt_result = None
    sqrt_option = input("which number you wanted to be squared, 1 for the first number, 2 for the second: ")    
    if sqrt_option=="1":
        if a<0:
            print("cant squar root a negative number!")
        else:
            sqrt_result = math.sqrt(a)
            print(f"The result of squar root {a}, is: {sqrt_result} ")
    elif sqrt_option=="2":
        if b<0:
            print("Can't squar root a negative number!")
        else:
            sqrt_result = math.sqrt(b)
            print(f"The result of squar root {b}, is: {sqrt_result} ")

    else: 
        print("unsupported input")
elif equation=="R":
    result = a%b    
else: 
    print("unsupported operation!")

#output
if result is not None:
    print(f"The result of {a} {equation} {b}, is: {result} ")


print("------------------------------------------------------------------")

 
