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
