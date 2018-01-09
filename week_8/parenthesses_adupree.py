# file: parentheses_adupree.py
# description: determine whether a expression contains matching parentheses
# author: Alexander DuPree
# date: 11 / 15 / 2017
# compiler: Python 3.6


def main():

    while True:
        print(intro())
        string = get_input(">  ")
        if matching(string) == True:
            print(output(string, True))
        else:
            print(output(string, False, missing_parens(string)))


def intro():
    return ("Enter a mathematical expression and I'll determine if it has"
            " matching parentheses\nType 'quit' to quit program\n")


def get_input(prompt):
    while True:
        string = input(prompt)
        if string.lower() == "quit":
            quit()
        elif '(' in string or ')' in string:
            return string
            break
        else:
            print("Error, your expression contains no parentheses")


def matching(string):
    return string.count("(") == string.count(")")


def missing_parens(string):
    if string.count("(") < string.count(")"):
        return ("{} left parentheses"
                .format(string.count(")") - string.count("(")))
    else:
        return ("{} right parentheses"
                .format(string.count("(") - string.count(")")))


def output(string, matching=False, missing=""):
    if matching == True:
        return "The expression: {} has matching parentheses!\n".format(string)
    else:
        return "The expression: {} is missing {}\n".format(string, missing)


main()
