# file: tuples_hackerrank_adupree.py
# description: tuples problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
Task
Given an integer,n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input

2
1 2
Sample Output

3713081631934410656
"""


def main():

    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))


main()
