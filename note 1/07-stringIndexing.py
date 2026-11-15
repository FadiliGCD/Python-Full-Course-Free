# indexing is accessing and element of a sequence using []
#[start : end : step]

name = "fadili bucharaya"

print(name[0])  #this will print charatere at index 0 of the string

print(name[0:3:1])  #this will print the first 3 charachters of the string #starting from index 0 to index 3 (the end idex is exclusive meaning it would not print)moving by 1 step

print(name[5:])     # from index5 to the end of the string

print(name[-1])     #this will print from the last index

#example print the last for digits of a credit card number
credit_number = "4848-5678-3949-4747"
credit_number_last_digits = credit_number[-4:]  
print(f"XXXX-XXXX-XXXX-{credit_number_last_digits}")
