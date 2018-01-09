#File: vote_adupree.py
#Description: Determines whether or not a person can vote
#Author: Alex DuPree
#Date: 10/16/2017
#Compiler: Python 3.6.3rc1

#########################################TEST VALUES##########################
"""
CAN YOU VOTE???

In the U.S., there are three criteria for voting.
Let me tell you if you are qualified.

Are you a U.S. citizen?  (yes or no)   Yes
How old are you? (in whole years)   21
Have you registered to vote?  (yes or no)   y
Congratualtions! You can vote!
"""
########################################RESET#################################

#In the U.S., there are three criteria for voting.
#Let me tell you if you are qualified.

#Are you a U.S. citizen?  (yes or no)   n
#How old are you? (in whole years)   123
#The greatest fully authenticated age to which any human has everlived is 
#122 years and 164 days by Jeanne Louise Calment
#, so... you'reprobably lying

######################################RESET###################################

#In the U.S., there are three criteria for voting.
#Let me tell you if you are qualified.

#Are you a U.S. citizen?  (yes or no)   n
#How old are you? (in whole years)   22
#Have you registered to vote?  (yes or no)   No
#You cannot vote. Maybe some day...

##################################END TEST VALUES#############################


print("CAN YOU VOTE???\n")

print("In the U.S., there are three criteria for voting.")
print("Let me tell you if you are qualified.\n")

citizen = input("Are you a U.S. citizen?  (yes or no)   ")

try:
	age = int(input("How old are you? (in whole years)   "))
except ValueError:
	print("Age must be inputed in whole integers.")
	exit()

if age > 122:
	print("The greatest fully authenticated age to which any human has ever "
	 "lived is 122 years and 164 days by Jeanne Louise Calment, so... you're"
	 "probably lying")
	exit()
elif age <= 0:
	print("Not sure how that works.")
	exit()

registered = input("Have you registered to vote?  (yes or no)   ")

if (citizen.lower() in ('n', 'no')) or (registered.lower() in ('n', 'no')) \
	or age < 18:
	print("You cannot vote. Maybe some day...")

else:
	print("Congratualtions! You can vote!")


