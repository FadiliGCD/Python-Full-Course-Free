#format specifiers = {value:flag} 
# we format the value based on the flag we use
#usefull falgs:
#.(number)f = #show decimal point in the amount (number)  # f means float
#:(number) = #alocat that many space
#:03 = #alocalt and zero pad that many spaces
#:< = left justify
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate positive value
#:= = use sign to leftmost position
#:  = insert space before positive numbers
#:, = comma seperator

number1 = 3.3848
number2= 56564.32324
number3 = -2.902

print(f"number is: {number1:.3f}") #diplay 3 number after coma
print(f"number is: {number2:10}")  #display 10 spaces including the number
print(f"number is: {number2:010}") #diplay 10 spaces including the number but fill the spaces with 0
print(f"number is: {number3:<10}") #left alligned in a space of 10
print(f"number is: {number3:>10}") #right alligned in a space of 10
print(f"number is: {number3:^10}") # center allinged in a space of 10
print(f"number is: {number2:,}") #coma for big numbers
#u can combin the falgs for a value
print(f"number is: {number2:,.2f}")