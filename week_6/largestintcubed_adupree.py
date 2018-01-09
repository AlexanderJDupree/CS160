# file: largestintCube_adupree.py
# description: Displays the largest ineteger of n**3 is less than 12000
# author: Alexander DuPree
# date: 11/01/2017
# compiler: Python 3.6


cubed = [n**3 for n in range(0, 100) if n**3 <= 12000]
print("22 is the largest integer that can be cubed and be less than 12,000. "
      "22 cubed is {}".format(max(cubed)))
