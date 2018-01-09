# file: lists_hackerrank_adupree.py
# description: Lists problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6


"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of i followed by n lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


def main():

    n = int(input())
    lst = []
    for x in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")" # creates string for eval method
            eval("lst." + cmd)
        else:
            print(l)


main()
