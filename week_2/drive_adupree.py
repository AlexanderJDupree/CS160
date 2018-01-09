#File: drive_adupree.py
#Description: Program determines if someone is eligible to drive
#Author: Alex DuPree
#Date: 10/11/2017
#Compiler: 3.4.1

def main():
    
    age = int(input("How old are you? "))

    exam = input("have you passed your drivers exam? ")

    if (age >= 16 and (exam.lower() in ('y', 'yes'))):
        print("You can drive")

    elif age <=0:
        print("Invalid number. Try again.")
        main()
    else:
        print("You cannot drive")

    print("\nDon't drink and drive.")


main()
