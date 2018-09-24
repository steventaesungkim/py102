print("Please fill in the blanks below:")
print("EX: (Name)'s favorite subject in school is (subject)!")
name = input("What is your name? ")
name = name.capitalize()
subject = input("Pick a subject. ")
subject = subject.capitalize()

final = "%s's favorite subject in school is %s!" % (name, subject)
print(final)
