#----------------------program for guessing number upto 3 digits------------#

import random
code_number = random.randint(1,999)
print("Welcome to the Guessing Game!\n")
print("I have a secret code between  0 and 999.\n")
print("You will 10 chance  to guess it.\n")
number = int(input('enter your first guess: '))
for i in range(10,0,-1):
    if number == code_number :
        print("\nCongratulations! You guessed correctly.")
        break
    elif number < code_number:
        print('Your guess is too low.')
    elif number > code_number:
        print('Your guess is too high.')
    number = int(input('Enter your next guess: '))
print(f'game end,the number was {code_number}.\n')