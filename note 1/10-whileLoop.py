# execute code while condition is true

name = input("Enter your name: ")

while name == "":
    print("you didn't enter anything.\nTry again!")
    name = input("Enter name again: ")
print(f"hy {name}")