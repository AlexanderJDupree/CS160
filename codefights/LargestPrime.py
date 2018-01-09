def prime_factors(n):
    """Find all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


primes = prime_factors(600851475143)
# The largest element in the prime factor list
largest_prime_factor = max(primes)
print(largest_prime_factor)
print(primes) # Print the prime factors out of curiousty
