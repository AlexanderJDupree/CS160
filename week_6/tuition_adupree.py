# file: tuition_adupree.py
# description:calculates the tuition cost ten years from now
# author: Alexander DuPree
# date: 11/01/2017
# compiler: Python 3.6


def main():
    tuition = 10000
    for n in range(10):
        tuition = tuition * 1.05

    print("In 10 years, the cost of 4 years tuition will be ${}"
          .format(round(tuition * 4, 2)))
    print("Have fun with those student loans!")


main()
