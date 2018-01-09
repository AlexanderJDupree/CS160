#File: story_adupree.py
#Description: Madlib style game asking user to fill in the story
#Author: Alex DuPree
#Date: 10/02/2017
#Compiler: Python 3.4.1

#Print program description, poll user for words to fill into the story

print("Crazy Story Program")
print("\nYou enter the indicated words, i'll tell you a story.\n")

adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter another adjective: ")
number = input("Enter a number: ")
noun_plural = input("Enter a plural noun: ")
verb = input("Enter a verb in -ing form: ")
noun_single = input("Enter a singular noun: ")

print("\nOK. Here is your story. . . \n")
print("It was a", adjective_1, "and", adjective_2, "night.")
print(number, noun_plural, "were", verb, "in the", noun_single + '.')
print("The end.")

