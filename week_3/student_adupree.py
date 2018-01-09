#File: student_adupree.py
#Description: Determine whether or not a person is enrolled in CS160.
#Author: Alex DuPree
#Date: 10/16/2017
#Compiler: Python 3.6.3rc1

#####################################TEST VALUES##############################
#SEARCH FOR A STUDENT

#Who are you looking for? (first and last name)  Ben Dover
#Members of the class:

#Sally Micheals
#Joe Roberts
#Kate Adams
#Alex DuPree

#Ben Dover is not in the class.

#######################################RESET##################################

#SEARCH FOR A STUDENT

#Who are you looking for? (first and last name)  alex dupree
#Members of the class:

#Sally Micheals
#Joe Roberts
#Kate Adams
#Alex DuPree

#alex dupree is in the class.

###################################END TEST VALUES############################


#creates list of students enrolled in CS160
students = ["Sally Micheals", "Joe Roberts", "Kate Adams", "Alex DuPree"]

print("SEARCH FOR A STUDENT\n")

search_query = input("Who are you looking for? (first and last name)  ")

print("Members of the class: \n")

for student in students:
	print(student)

#converts student names to lower case for searching
students = [x.lower() for x in students]

if search_query.lower() in students:
	print("\n{} is in the class.".format(search_query))

else:
	print("\n{} is not in the class.".format(search_query))
