import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

output = [rock,paper,scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
com = random.randint(0,2)
print(output[you])
print("Computer chose:")
print(output[com])
if you >= 3 or you < 0: 
  print("You typed an invalid number, you lose!") 
elif you == 0 and com == 2:
  print("You win!")
elif com == 0 and you == 2:
  print("You lose")
elif com > you:
  print("You lose")
elif you > com:
  print("You win!")
elif com == you:
  print("It's a draw")
