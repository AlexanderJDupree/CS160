# file: strign_functions_worksheet_adupree.py
# description: list and description of string methods
# author: Alexander DuPree
# date: 11 / 13 / 2017
# compiler: Python 3.6

phrase = "Go Seahawks!"

# 2
print(phrase.title())  # Go Seahawks!
# Changes the first letter of each word to uppercase

# 3
print(phrase.lower())  # go seahawks!
# changes the sting to all lowercase

# 4
print(phrase[0].isalpha())  # True
# checks if character at index 0 in phrase is alphabetic, returns boolean value

# 5
print(phrase[0].isnumeric())  # False
# checks if character at index 0 in phrase is numeric, returns boolean value


# 6
print(phrase[0].isupper())  # True
# checks if character at index 0 in phrase is uppercase, returns boolean value

# 7
print(phrase[0].islower())  # False
# checks if character at index 0 in phrase is lowercase, returns boolean value

# 8
print(phrase[0].isspace())  # False
# checks if character at index 0 in phrase is a space, returns boolean value

# 9
print(phrase.replace("a", "X"))  # Go SeXhXwks!
# Replace all 'a' characters with 'X' characters in the string

# 10
print(phrase.count('a'))  # 2
# Counts the number of times character 'a' appears, returns integer value

# 11
print(phrase.strip('!'))  # Go Seahawks
# Strips the special character '!' from string, returns stripped string

# 12
print(phrase[0].isdigit())  # False
# checks if character at index 0 in phrase is a digit, returns boolean value

# 13
print(phrase[0].isdecimal())  # False
# checks if character at index 0 in phrase is base 10 number, returns boolean value

# 14
print(phrase.split())  # ['Go', 'Seahawks!']
# Splits the string at the space character and appends each element to a list,
# returns the list.
