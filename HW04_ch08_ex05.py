# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
#
#
# Caesar cypher
#
########################################################################

def rotate_word(word, rotate_by):
    """Returns an encrypted word by rotating each letter by some given
    amount.
    
    Parameters:
    word -- the original word to encrypt
    rotate_by -- an integer amount by which to rotate each letter
    """
    
    a = 97
    z = 122
    upper_a = 65
    upper_z = 90
    new_word = ""
    
    if rotate_by < 0:
        rotate_by = rotate_by % 26

    for letter in word:
        if letter.islower():
            new_pos = (ord(letter) + (rotate_by)) % z
            if new_pos < a:
                new_pos += a - 1
            new_letter = chr(new_pos)
        else:
            new_pos = (ord(letter) + (rotate_by)) % upper_z
            if new_pos < upper_a:
                new_pos += upper_a - 1
            new_letter = chr(new_pos)
        new_word += new_letter
    return new_word

def main():
    print(rotate_word("IBM", -1))
    print(rotate_word("abc", 27))
    print(rotate_word("aBc", 1))
    print(rotate_word("cheer", 7))
    print(rotate_word("melon", -10))
    print(rotate_word("melon", -36))
    print(rotate_word("apple", 0))
    
if __name__ == "__main__":
    main()