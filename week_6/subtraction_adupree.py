# file: subtraction_adupree.py
# description:subtraction game
# author: Alexander DuPree
# date: 11/01/2017
# compiler: Python 3.6

"""
Write a program to play a subtraction game. The game should run as many times as the user desires (ask the user how many games to play at the beginning of the program). Each time the game runs, the user should be presented with a random subtraction problem, using positive integers. The computer should keep track of how many answers the user answered correctly and output that number at the end of the program.
"""

from random import randrange


def main():
    intro()
    games = sanitised_input(
        "How many games would you like to play?  ", int, 1)
    print("you got {}/{} correct!".format(subtraction_game(games), games))


def intro():
    print("\n\tSUBTRACTION GAME\n")
    print("This game will present you with a random subtraction problem enter the answer and I'll tell you if you're right!\n")


def subtraction_game(num):
    num_correct = 0
    guesses = 0
    while guesses < num:
        num1 = randrange(20)
        num2 = randrange(20)
        answer = num1 - num2
        print("\n{} - {} = ???".format(num1, num2))
        guess = sanitised_input("> ", int)
        if guess == answer:
            num_correct += 1
        guesses += 1
    return num_correct


def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join((", ".join(map(str,
                                                                     range_[:-1])),
                                                       str(range_[-1])))))
        else:
            return ui


main()
