#File: slope_adupree_extracredit.py
#Description:Computes the slope of a line given two poitns
#Author:Alex DuPree
#Date: 10/06/2017
#Compiler: 3.4.1

#Poll user for x1, x2, y1, y2 coordinate points

x1 = float(input("X coordinate for first point? "))
y1 = float(input("Y coordinate for first point? "))
x2 = float(input("X coordinate for second point? "))
y2 = float(input("Y coordinate for second point? "))

slope = (y2 - y1)/(x2 - x1)

print("The slope of the line going through points ({}, {}),({},{}) is {}".format(x1,y1,x2,y2,slope))
