# file: sting_hackerrank_adupree.py
# description: find occurances of a string problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
"""


def count_substring(string, sub_string):
    counter = 0
    for c, i in enumerate(string):
        if i == sub_string[0]:  # signifies start of substring
            if string[c:c + len(sub_string)] == sub_string:  # checks if pattern matches
                counter += 1
    return counter


print(count_substring('ABCDCDC', 'CDC'))
