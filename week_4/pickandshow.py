# file: pickAndShowRev1_adupree.py
# description: Asks user to open file, opens picture file, displays it
# author: Alex DuPree
# date: 10 / 20 / 2017
# compiler: JES 5.01


def main():
    intro()
    choice = raw_input("Open a file? ")
    if choice.lower in ('n', 'no'):
        print("Have a nice day!")
        quit()
    else:
        show_image(make_image(get_file()))


def get_file():
    return pickAFile()


def make_image(file):
    return makePicture(file)


def show_image(image):
    return show(image)


def intro():
    print("\n\tOPEN AND DISPLAY A IMAGE FILE\n")


main()
