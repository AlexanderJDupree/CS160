# file: rewardPoints_adupree.py
# description: Program to determine reward points
# authors: Alex DuPree
# date: 11/20/2017
# compiler: Python 3.6


def main():
    intro()
    func, spent = get_input()
    points = eval(func + '(spent)')
    display_points(points)


def standard(spent):
    if spent < 75:
        return int(spent * .05)
    elif spent > 75 and spent < 150:
        return int(spent * .075)
    else:
        return int(spent * .10)


def plus(spent):
    if spent < 150:
        return int(spent * .06)
    else:
        return int(spent * .13)


def premium(spent):
    if spent < 200:
        return int(spent * .04)
    else:
        return int(spent * .15)


def get_input():
    while True:
        membership = input(
            "\nWhat is you membership type: Standard, Plus, or Premium?  ")
        if membership.lower() in ('standard', 'plus', 'premium'):
            break
        else:
            continue
    while True:
        try:
            spent = int(
                input("\nHow much money have you spent in store this month:  "))
        except ValueError:
            print("Error: input must be positive integers only")
        if spent > 0:
            break
        else:
            print("Error: input must be positive INTEGERS only")

    return membership.lower(), spent


def display_points(points):
    print("Reward points earned:  {}\n\nThank you for shopping!".format(points))


def intro():
    print("\tREWARD POINTS\n")
    print("This app to determines how many reward points you have earned this month")


main()
