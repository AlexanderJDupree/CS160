#File:conversion_adupree.py 
#Description: Converts a number of feet (entered by the user) to meters
#Author: Alex DuPree
#Date: 10/02/2017
#Compiler: Python 3.4.1

#Print description of program then poll user for input data
print("Feet to Meters\n")
print("This program will convert a number of feet to meters.\n")

feet = float(input("How many feet would you like to convert? "))

meters = feet * 0.3048

#prints coversion statement as a string

print(str(feet),"feet =", str(meters), "meters")
