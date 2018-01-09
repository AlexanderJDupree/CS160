#File: larger_adupree.py
#Description: Determines which of two integers is larger.
#Author: Alex DuPree
#Date: 10/16/2017
#Compiler: Python 3.6.3rc1

#######################################TEST VALUES############################
#FIND THE LARGER NUMBER

#Enter two whole numbers & I will tell you which is larger.

#First number:  6
#Second number:  4
#The first number is larger

######################################RESET###################################
#Enter two whole numbers & I will tell you which is larger.

#First number:  34
#Second number:  jack and jill went up the hill

#You must input an integer

#####################################RESET####################################
#Enter two whole numbers & I will tell you which is larger.

#First number:  3
#Second number:  3
#the two numbers are the same

######################################END TEST VALUES#########################

print("FIND THE LARGER NUMBER\n")

print("Enter two whole numbers & I will tell you which is larger.\n")

try:
    first_number = int(input("First number:  "))
except ValueError:
    print("\nYou must input an integer")
    exit()
try:
    second_number = int(input("Second number:  "))
except ValueError:
    print("\nYou must input an integer")
    exit()

if first_number > second_number:
    print("The first number is larger")

elif first_number < second_number:
    print("The second number is larger")

else:
    print("the two numbers are the same")
