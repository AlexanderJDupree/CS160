# File: decrypt_adupree.py
# Description: Encrypts a four digit number
# Author: Alex DuPree
# Date: 10/16/2017
# Compiler: Python 3.4.1


def decrypt():

    print("\nEnter the encrypted integer i.e.(1.00.10.80.9)")
    encrypted = input('> ')

    if len(encrypted) != 12:
        print("Invalid input. incorrect number format.")
        exit()

    # intiates a null list for the string to be broken into
    num = []

    n = 3

    while n <= len(encrypted):
        num.append(encrypted[n - 3:n])
        n += 3

    # tries converts list of strings to a list of floats
    try:
        num = list(map(float, num))
    except ValueError:
        print("Invalid input. incorrect number format.")
        exit()

    for n in range(len(num)):
        if num[n] <= .6:
            num[n] = num[n] + 1
        num[n] = num[n] * 10 - 7

    # converts list into integers to get rid of the .0
    num = list(map(int, num))
    # Unscrambles list indexes
    num[0], num[1], num[2], num[3] = num[2], num[3], num[0], num[1]

    # Prints the decrypted integer as a string
    decrypted_integer = map(str, num)

    print("\nYour decrypted integer is", ''.join(decrypted_integer))


decrypt()
