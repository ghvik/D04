#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (in the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """This is wrong because the function will exit immediately after checking
    only the first letter in the string. If the first letter is uppercase, it
    will return False without checking the other letters (which may or may not
    be lowercase).
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """This is wrong for 3 reasons. First, the function will again exit out of 
    the for loop after only checking one letter. However, that letter will not 
    be the first letter of the string as intended. Instead, it will always be
    'c', which is lowercase, so the function will return immediately 'True'.
    This return value is a string instead of a boolean, which is the final
    error.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This is wrong because the boolean flag changes at each letter, and the 
    function will only return the most recent flag. So it essentially only
    checks if the last letter is lowercase. It will have an error if the last
    letter is uppercase and any of the previous letters are lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Nothing is wrong.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """This is wrong because it will exit out of the function as soon as it 
    reaches an uppercase letter. So it will fail if a string has a lowercase
    letter that appears after an uppercase letter.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("Apple"))
    print(any_lowercase2("SOS"))
    print(any_lowercase3("helP"))
    print(any_lowercase5("Uptown"))

if __name__ == '__main__':
    main()
