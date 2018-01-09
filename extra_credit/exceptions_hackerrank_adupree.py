# file: exceptions_hackerrank_adupree.py
# description: exception handling problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
Task

You are given two values A and B.
Perform integer division and print .

Input Format

The first line contains n, the number of test cases.
The next  lines each contain the space separated values of A and B.


Output Format

Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""


def main():
    n = int(input())
    for _ in range(n):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)


main()
