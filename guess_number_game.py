# Guessing Game

# Program picks a random integer from 1 to 100 and player has to guess the number.

# The rules are:
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is:
#   - within 10 of the number, return "WARM"
#   - further than 10 away from the number, return "COLD"
# 3. On all subsequent turns, if a guess is:
#   - closer to the number than the previous guess return "WARMER"
#   - farther from the number than the previous guess, return "COLDER"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took.

import random

number = random.randint(1,100)
print(number)
num_of_guesses = 0
diff = None # absolute difference between the guess and the number

while True:
    guess = int(input('Guess the number from 1 to 100.\n'))
    num_of_guesses += 1

    if guess < 1 or guess > 100:
        num_of_guesses -= 1 # wrong guess
        print('OUT OF BOUNDS')
        continue
    elif num_of_guesses == 1: # first guess scenario
        diff = abs(number-guess)
        if guess == number:
            print('Are you a witch? How do you know what number I have in mind?')
            break
        elif diff <= 10:
            print('WARM')
        else:
            print('COLD')
    elif guess == number: # after first guess scenario
        print(f'Good job! You guessed after {num_of_guesses} tries.')
        break
    else:
        prev = diff
        diff = abs(number-guess)
        if prev > diff: print('WARMER')
        else: print('COLDER')