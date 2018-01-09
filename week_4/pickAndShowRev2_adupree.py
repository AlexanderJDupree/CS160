# file: pickAndShowRev2_adupree.py
# description: Asks user to open file, opens picture file, displays it
# author: Alex DuPree
# date: 10 / 20 / 2017
# compiler: JES 5.01


def main():
    intro()
    choice = raw_input("\nOpen a file? ")
    if choice.lower() in ('n', "no"):
        print("Have a nice day!")
        quit()
    elif choice.lower() in ('y', "yes"):
        show_image(make_image(get_file()))
    else:
        print("Sorry, did not recognize input. Try again")
        main()
    closing()


def get_file():
    return pickAFile()


def make_image(file):
    return makePicture(file)


def show_image(image):
    try:
        return show(image)
    except java.lang.NullPointerException:
        print("ERROR: Wrong file type")
        quit()


def intro():
    print("\n\tOPEN AND DISPLAY AN IMAGE FILE\n")
    print("This program will prompt you wheter or not you would like to open a file")


def closing():
    print("\nThank you for using my program! Have a nice day!")


main()
