# file: nth_prime_euler_adupree.py
# description: Find the nth prime number.
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
FROM PROJECT EULER:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Erastothenes sieve is what this algorithim is based of off.


def nth_prime_number(n):
    # initial prime number list
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


print(nth_prime_number(10001))
