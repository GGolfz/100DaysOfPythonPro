import random
from Hangman_art import stages
from Hangman_words import word_list

chosen_word = random.choice(word_list)
display = []

for _ in chosen_word:
    display += '_'
print(" ".join(display))
lives = len(stages) - 1
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    found = False
    for pos in range(len(chosen_word)):
        if guess == chosen_word[pos]:
            found = True
            if display[pos] == '_':
                display[pos] = chosen_word[pos]
            else:
                print(guess,"already choose!")
                break
    if not found:
        lives -= 1
        print(guess,"is not in the word.")
    print(" ".join(display))
    print(stages[lives])
if lives > 0:
    print("Congratulations !")
else:
    print("You lose !")