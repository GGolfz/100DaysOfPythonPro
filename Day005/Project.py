import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
pools = []
for i in range(nr_letters):
    pools.append(letters[random.randint(0,len(letters))])
for i in range(nr_symbols):
    pools.append(symbols[random.randint(0,len(symbols))])
for i in range(nr_numbers):
    pools.append(numbers[random.randint(0,len(numbers))])
# Easy Version
# for i in range(0,len(pools)):
#     password += pools[i]
# Hard Version
for i in range(0,len(pools)):
    index = random.randint(0,len(pools)-1)
    password += pools[index]
    pools.pop(index)

print("Here is your password: "+str(password))