# file: calculator_adupree.py
# description: Returns basic calculator operations to user
# author: Alexander DuPree
# date: 10/23/2017
# compiler: JES 5.01


def main():
    intro()
    num1 = get_num()
    num2 = get_num()
    operator = operation()
    if operator == '+':
        show_answer(num1, num2, operator, addition(num1, num2))
    elif operator == '-':
        show_answer(num1, num2, operator, subtraction(num1, num2))
    elif operator == '/':
        show_answer(num1, num2, operator, division(num1, num2))
    elif operator == '*':
        show_answer(num1, num2, operator, multiplication(num1, num2))


def operation():
    print("\nEnter a mathematical operator i.e. (+, - , /, *")
    operator = raw_input(">  ")
    if operator in ('+', '-', '/', '*'):
        return operator
    else:
        print("Invalid input")
        exit()


def get_num():
    try:
        num = float(input("Enter a number:  "))
    except ValueError:
        print("Error: Invalid input")
    return num


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        print("Error cannot divide by 0")
        quit()
    else:
        return num1 / num2


def show_answer(num1, num2, operator, num3):
    print("%d %s %d = %d" % (num1, operator, num2, num3))


def intro():
    print("\n\tCALCULATOR APPLICATION FOR PYTHON\n")
    print("This application takes two numbers and an operation and will"
          " return a value")


main()
