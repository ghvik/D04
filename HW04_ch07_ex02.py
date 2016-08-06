#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import pdb

# Body
def eval_loop():
    result = ""
    while True:
        # Prompt user
        prompt = ("Please type some Python code to evaluate or type 'done' to finish:\n")
        user_input = input(prompt)
        
        # Evaluate result
        if user_input != "done":
            try:
                result = eval(user_input)
            except (SyntaxError, NameError) as e:
                print("Please check if there are any syntax errors or undefined variables in your code.", e)
            print(result)
        else:
            return result

###############################################################################
def main():
    eval_loop()
    
    # Uncomment to test the return value of the last evaluated expression
    # print(eval_loop()) 

if __name__ == '__main__':
    main()
