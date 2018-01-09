# file:largest_palindrom_product_euler_adupree.py
# description: Find the largest palindromic product of a 3 digit number.
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6


# Create a palindrom check function
# Check for largest palindrome in range of 100-1000

"""
FROM PROJECT EULER:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(num):
    return str(num) == str(num)[::-1]


def largest(bottom, top):
    # Loop through every combination of multiplies from a 3 digit number
    z = 0
    for x in range(top, bottom, -1):
        for y in range(top, bottom, -1):
            if palindrome(x * y):
                if x * y > z:
                    z = x * y
    return z


print(largest(100, 1000))
