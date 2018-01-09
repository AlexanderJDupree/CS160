# file: stringsInClass_adupree.py
# description: Manipulates user string
# author: Alexander DuPree
# date: 11 / 13 / 2017
# compiler: Python 3.6


class user_input:
    '''Creates object with all user choices and inputs'''

    def __init__(self, run_program=True, string="", function_index=""):
        self.run_program = run_program
        self.string = string
        self.function_index = function_index

    def string_functions(self):
        options = {
            1: self.string.upper(),
            2: self.string.title(),
            3: self.string.lower(),
            4: self.string.split(),
            5: self.string.count('a'),
            6: self.string.strip('a'),
            7: self.string.replace('a', 'X'),
            8: self.string.replace(" ", '').isalpha(),
            9: self.string.replace(" ", '').isnumeric(),
            10: self.string.replace(" ", '').isupper(),
            11: self.string.replace(" ", '').islower(),
            12: self.string.replace(" ", '').isdigit(),
            13: self.string.replace(" ", '').isdecimal(),
            14: self.string[self.string.find(" ")].isspace()
        }

        return options[self.function_index]

    def show_string(self):
        print("\nOriginal string:", self.string)
        print("Function return:", self.string_functions())


def main():

    ui = user_input()
    while ui.run_program == True:
        ui.string = get_string(">  ")
        ui.function_index = function_choice()
        ui.show_string()
        ui.run_program = repeat_program(">  ")
    return 0


def repeat_program(prompt):
    print("\nRun the program again?? yes or no")
    while True:
        choice = input(prompt)
        if choice.lstrip().rstrip().lower() in ('y', "yes"):
            return True
            break
        elif choice.lower() in ('n', "no"):
            return False
            break


def get_string(prompt):
    while True:
        print("\nEnter a string, string must contain numbers and letters ONLY.")
        string = input(prompt)
        if is_alphanumeric(string) == True:
            return string
            break
        else:
            print("Error: No special characters allowed, i.e. ! @ $. etc.")


def is_alphanumeric(string):
    return string.replace(" ", "").isalnum()


def function_choice():
    print("""
        Choose a function from the list:
        1. upper(), returns a string in uppercase
        2. title(), returns a titlecased version of the string
        3. lower(), returns a string in lowercase
        4. split(), returns a list with each word of the string
        5. count('a'), counts occurrences of 'a' character in string
        6. strip('a'), removes any occurrences of 'a' in string
        7. replace('a', 'X'), replaces any 'a' with an 'X' character

        options 8 - 14 return True or False values

        8. isalpha(), checks if entire string is alphabetic
        9. isnumeric(), checks if entire string is numeric
        10. isupper(), checks if entire string is uppercase
        11. islower(), checks if entire string is lowercase
        12. isdigit(), checks if entire string is digits
        13. isdecimal(), checks if entire string is composed of decimal numbers
        14. isspace(), checks if there is any spaces in the string\n
        Enter corresponding number for function choice.
        """)

    while True:
        try:
            choice = int(input(">  "))
        except ValueError:
            print("Error: input must be integers between 1 - 14")
            continue

        if choice > 14 or choice < 1:
            print("Error: input must be integers between 1 - 14")
            continue
        else:
            break
    return choice


main()
