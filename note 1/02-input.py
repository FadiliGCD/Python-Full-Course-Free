#this program collects information from a user and displays a personilized registration summary


#welcome message
print("Welcome to the User Registration System")

#obtain user details: full name, age, country and date of birth
user_name = str(input("Please enter your name: "))
user_lastname = str(input("Please enter you last name: "))
user_age = int(input("Please enter your age: "))
user_country = str(input("Please enter your country: "))
user_birthday = int(input("what day where you born: "))
user_birthmonth = int(input("what month where you born: "))
user_birthyear = int(input("what year were you born: "))


#Users age in 2030
user_ageIn2030 = 2030 - user_birthyear

#terminal output
print("--------------REGISTRATION SUMMARY-------------------\n"
      f"Full name: {user_name} {user_lastname}\n"
      f"Age: {user_age}\n"
      f"Country: {user_country}\n"
      f"In 2030 you will be {user_ageIn2030} years old, on day {user_birthday} of month {user_birthmonth}\n"
      "----------------------------------------------------\n"
    )
