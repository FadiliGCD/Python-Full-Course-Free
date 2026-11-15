# COMPOUND INTERST CALCULATOR

#welcom user
print("\n--------------COMPOUND INTERST CALCULATOR--------------\nWelcome!")

#********************initial investment input logic****************************************
investment = input("\nWhat is your initial investment in euros: ")

#print(type(investment))   for debugging
while not investment.isdigit():
    print("you can't enter letters\nTry again: ")
    investment = input("What is you initial investment in euros: ")

#print(f"2{type(investment)}")   for debugging
investment = float(investment)

#print(f"3{type(investment)}")    fro debugging
while investment <= 0:
    print("investment Can't be negative or equal to zero.\nTry again: ")
    investment = float(input("What is you initial investment in euros: "))
#bug: the .isdigit() fonction counts negative numbers as a string


#anuan intrest rate input logic
anual_intrest_rate = input("\nWhat is your anual intrest rate%(enter it in form of 56.97, whithout the percentage sign): ")

while not anual_intrest_rate.isdigit():
    print("you can't enter letters\nTry again: ")
    anual_intrest_rate = input("What is your anual intrest rate%: ")
    #bug: 65.3 stored as str data type

anual_intrest_rate = float(anual_intrest_rate)

while anual_intrest_rate < 0:
    print("intrest rate Can't be negative or equal to zero.\nTry again: ")
    anual_intrest_rate = float(input("What is your anual intrest rate%: "))


numnber_of_years = input("enter numbers of years: ")

#number of years input logic
while not numnber_of_years.isdigit():
    print("please enter numbers!\nTry again: ")
    numnber_of_years = input("enter number of years: ")
    #bug : 45.3 stored as str data type

numnber_of_years = float(numnber_of_years)

while numnber_of_years <= 0:
        print("number of years cant be negative or zero\nTry again: ")
        numnber_of_years = float(input("enter number of years: "))

#frequenct input logic

print("\nSelect compounding frequency:\n1. Annually\n2. Quarterly\n3. Monthly\n4. Daily\n(answer with either 1,2,3 or 4)")
frequency = input("whats the frequency: ")


while not frequency.isdigit():
     print("Can't enter a letter!\ntry again: ")
     frequency = input("whats the frequency: ")

frequency = int(frequency)

while frequency < 1 or frequency > 4:
     print("please choose from 1 to 4: ")
     frequency = int(input("whats the frequency: "))
     #bug: if you enter a str now, the program crashes
frequency = int(frequency)


#final investemt value logic
print("---------------- INVESTMENT SUMMARY ----------------")
print(f"Initial invetment: {investment:,}\nAnual intrest rate: {anual_intrest_rate:2f}\nDuration: {numnber_of_years}years\nCompounding: {frequency:^10}")
final_balance = investment*(1+(float(anual_intrest_rate))/numnber_of_years)**frequency
print(f"final balace: {final_balance}\n-------------------------------")


