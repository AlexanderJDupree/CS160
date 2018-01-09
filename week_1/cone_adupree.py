# File: cone_adupree.py
# Description:Computes and outputs the volume of a cone
# Author:Alex DuPree, Alex Hoang
# Date: 10/06/2017
# Compiler: 3.4.1

# defines pi constant
from math import pi

# Poll user for radius, and height data for cone, print program description

print("This program computes the volume of a cone given the diameter of its"
      "base and height from the user")

radius = float(input("\nEnter the diameter: ")) / 2
# computes radius by halving diameter

height = float(input("\nEnter the height: "))

# computes volume using below formula
volume = (1 / 3) * pi * radius ** 2 * height
# prints volume of cone to display
print("\nThe volume of the cone is", volume, "units cubed")
