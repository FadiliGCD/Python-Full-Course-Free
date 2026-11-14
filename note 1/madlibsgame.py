print("----------------Welcom to MADLIBS Game--------------------\n"
      "To start this game you will have add few details, by the answering these questions\n"
      "Are You ready?"
    )

ready = input("y or n? ")

if ready=="y" :
    print("---AWESOME---")
    name = input("give a name: ")
    adjective = input("give an adjective: ")
    company = input("give a company: ")
    food = input("give a food: ")
    animal = input("give an animal: ")
    programming_language = input("give a programming language: ")
    verb = input("give a verb: ")
    salary = int(input("give a salary: "))

    print("---------THE CRAZY JOB INTERVIEW-----------------\n"
          f"One day, {name} woke up feeling extremely {adjective}\n"
          f"because today was their first job interview at {company}.\n"
          "\n"
          f"They quickly ate a {food} for breakfast and travelled\n"
          f"to the office on a {animal}.\n"
          "\n"
          "When the interviewer asked, 'What programming language do you know?'\n"
          f"they confidently answered, '{programming_language}'!\n"
          f"The interviewer was so surprised that they started to {verb}.\n"
          f"In the end, {name} was offered a salary of €{salary}\n"
          "per year, and everyone lived happily ever after."

    )
else: 
    print("Well see you next time!")
