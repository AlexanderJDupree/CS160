# file: nestedlist_hackerrank_adupree.py
# description: Nested lists problem set for hackerrank
# authors: Alex DuPree
# date: 11/17/2017
# compiler: Python 3.6


"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output

Berry
Harry
Explanation

There are  students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""


def main():

    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]
    students.sort(key=lambda student: abs(student[1]))
    while students[0][1] == students[1][1]:
        students.pop(0)
    students.pop(0)
    names = [x for x in students if x[1] == students[0][1]]
    names.sort(key=lambda names: names[0])
    for name in names:
        print(name[0])


main()
