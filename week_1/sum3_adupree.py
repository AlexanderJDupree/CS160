#File:sum3_adupree.py
#Description:Compute the sum of three numbers inputed by the user
#Author: Alex DuPree
#Date: 10/02/2017
#Compiler: Python 3.4.1

#Poll user for three numbers, store them into variables.
print("Sum of Three Numbers\n")

number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
number_three = int(input("Enter a third number: "))

sum3 = number_one + number_two + number_three

#Prints the sum of the three numbers to the shell
print("\nThe sum of those values is", str(sum3)+'.')
