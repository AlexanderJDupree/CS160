# File: crypt_adupree.py
# Description: Encrypts a four digit number
# Author: Alex DuPree
# Date: 10/16/2017
# Compiler: Python 3.4.1


def encrypt():
    # Creates a list from the four digit integer
    num = input("Enter a four digit integer: ")

    if len(num) != 4 or (is_number(num) == False):
        print("Invalid integer, integer must be postive and only have 4 digits")
        exit()

    num = list(num)

    # Swap the first digit with the third and swap the second digit with the fourth.
    num[0], num[1], num[2], num[3] = num[2], num[3], num[0], num[1]

    # Replace each digit with the result of adding 7 to the digit and getting the
    # remainder after dividing the new value by 10
    for n in range(len(num)):
        num[n] = (int(num[n]) + 7) / 10
        if num[n] > 1:
            num[n] = round(num[n] - 1, 2)

    # Prints the encrypted integer as a string
    encrypted_integer = map(str, num)
    print("\nYour encrypted integer is", ''.join(encrypted_integer))


# Defines a function to check if input is an integer
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


encrypt()
