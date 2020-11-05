print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
first = 0
sec = 0
name1 = name1.lower()
name2 = name2.lower()
first += name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
first += name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
sec += name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
sec += name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
love = first*10 + sec
if love < 10 or love > 90:
    print("Your score is "+str(love)+", you go together like coke and mentos.")
elif love >= 40 and love <= 50:
    print("Your score is "+str(love)+", you are alright together.")
else:
    print("Your score is "+str(love))