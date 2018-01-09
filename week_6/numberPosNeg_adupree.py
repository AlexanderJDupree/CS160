# file: numberPosNeg_adupree.py
# description:Returns the number of positve and negative numbers entered
# author: Alexander DuPree
# date: 11/01/2017
# compiler: Python 3.6


def main():
    pos, neg = input_and_count()
    print("You entered {} positve integer(s), and {} negative integer(s)".format(pos, neg))
    print("Thank you for using my program!")


def input_and_count():
    pos = 0
    neg = 0
    while True:
        num = sanitised_input(
            "Enter a number: (0 will terminate input sequence)\n>", int)
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            break
    return pos, neg


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
