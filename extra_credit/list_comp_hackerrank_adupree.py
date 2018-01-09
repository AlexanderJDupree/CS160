# file: list_comp_hackerrank_adupree.py
# description: list comprehension problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6

"""
Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. You have to print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of  is not equal to n.

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1)
           for k in range(z + 1) if((i + j + k) != n)])


main()
