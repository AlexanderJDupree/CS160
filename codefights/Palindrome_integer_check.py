# Create a palindrom check function
# Check for largest palindrome in range of 100-1000


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
