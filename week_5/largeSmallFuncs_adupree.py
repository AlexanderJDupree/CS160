# file: largeSmallFuncs_adupree.py
# description: output the largest and smallest number
# author: Alexander DuPree
# date: 10/23/2017
# compiler: JES 5.01


def main():
    numbers = []
    intro()
    for n in range(3):
        numbers.append(get_number())
    show_large_small(numbers)


def get_number():
    try:
        num = int(input("Enter a number:  "))
    except ValueError:
        print("ERROR: input integers only")
        quit()
    return num


def find_smallest(nums):
    return min(nums)


def find_largest(nums):
    return max(nums)


def show_large_small(nums):
    print("\nThe largest number is %r \nThe smallest number is %r"
          % (find_largest(nums), find_smallest(nums)))


def intro():
    print("This program will output the largest and smallest number "
          "from a sequence of numbers.\n")


main()
