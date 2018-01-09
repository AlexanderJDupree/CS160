#File:tip_adupree.py
#Description: Computes the tip for a restaurant meal
#Author: Alex DuPree
#Date: 10/02/2017
#Compiler: Python 3.4.1

#Print program description, poll user for bill
print("Tip calculator\n")
print("This program will tell you how much tip you should pay, assuming the service was good, but not exceptional.\n")

bill = float(input("How much was the bill for the meal? "))

#Calculates the tip at 15% rate and computes the total bill
tip = bill * 0.15

total_bill = bill + tip

#Prints the tip and total bill back to user
print("\nThe tip, computed at 15%, is $" + str(tip) + '.')
print("\nThe total bill is $" + str(total_bill) + '.')
