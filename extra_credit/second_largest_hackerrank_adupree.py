# file: second_largest_hackerrank_adupree.py
# description: find the second largest number problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
You are given n numbers. Store them in a list and find the second largest number.

Input Format

The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

Output Format

Print the value of the second largest number.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5

Explanation:
Given list is [2 3 6 6 5]. The maximum number is 6, second maximum is 5. Hence, we print 5 as our answer.
"""


def main():

    n = int(input())
    array = list(set(map(int, input().split())))
    array.pop(array.index(max(array)))
    print(max(array))


main()
