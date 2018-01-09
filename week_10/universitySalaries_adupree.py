# file: univirsitySalaries_adupree.py
# description: Outputs the highest paid employee of the Indiana university system
# author: Alexander DuPree
# date: 12/02/2017
# compiler: Python 3.6

from textwrap import dedent

def main():
    employee, position = find_highest_paid('IndianaSalaries.csv')
    output(employee, position)

def find_highest_paid(filename):
    with open(filename, 'r') as f:
        next(f) # Skips fieldnames
        file = [line.split('"') for line in f.readlines()]
        highest_salary = 0
        index = 0
        for n, line in enumerate(file):
            try:
                salary = int(''.join(e for e in line[3] if e.isdigit()))
                if salary > highest_salary:
                    highest_salary = salary
                    index = n
            # Row 512 is formatted differently and throws an index error
            except IndexError:
                salary = int(''.join(e for e in line[1] if e.isdigit()))
                if salary > highest_salary:
                    highest_salary = salary
                    index = n
        return file[index], file[index][-1].split(',')

def output(employee, position):
    print(dedent("""
            The highest paid employee of the Indiana university system is:
            NAME: {}
            SALARY: {}
            UNIVERSITY OR OFFICE: {}
            POSITION: {}
            """.format(employee[1], employee[3], position[1], position[2])))

main()
