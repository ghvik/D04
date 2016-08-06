#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint

# Body
def guess_the_number():
    num = randint(1, 25)
    prompt = ""
    for n in range(1,6)[::-1]:
        prompt = ("Please guess a number from 1 to 25, inclusive. You have {} {} left. "
            .format(n, "tries" if n > 1 else "try"))
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Sorry, that's not a number. Please enter it using digits.")
        else:
            if num == user_input:
                print("Congrats, you guessed it right!")
                break
            if n == 1:
                # Do not give the user another hint if they are out of tries
                continue
            if num > user_input:
                print("Please guess a higher number. ")
            else:
                print("Please guess a lower number. ")
    else:
        print("Sorry, you are out of tries.")
        


################################################################################
def main():
    guess_the_number()

if __name__ == '__main__':
    main()