from random import randint


def main():
    file = pickAFile()
    pic = makePicture(file)
    choose_function(pic)
    show(pic)


def choose_function(pic):
    print("""\nlessRed = 1
            lessBlue = 2
            lessGreen = 3
            moreBlue = 4
            moreGreen = 5
            darken = 6
            clearRed = 7
            clearBlue = 8
            clearGreen = 9
            myColorChange = 10 (this one is cool)
            blacktoWhite = 11""")
    choice = sanitised_input("Choose a function from the list:  ", int, 0, 11)
    if choice == 1:
        lessRed(pic)
    elif choice == 2:
        lessBlue(pic)
    elif choice == 3:
        lessGreen(pic)
    elif choice == 4:
        moreBlue(pic)
    elif choice == 5:
        moreGreen(pic)
    elif choice == 6:
        darken(pic)
    elif choice == 7:
        clearRed(pic)
    elif choice == 8:
        clearBlue(pic)
    elif choice == 9:
        clearGreen(pic)
    elif choice == 10:
        myColorChange(pic)
    elif choice == 11:
        blackToWhite(pic)


def lessRed(pic):
    for px in getPixels(pic):
        red_val = getRed(px)
        setRed(px, red_val - 150)


def lessBlue(pic):
    for px in getPixels(pic):
        blue_val = getBlue(px)
        setBlue(px, blue_val - 150)


def lessGreen(pic):
    for px in getPixels(pic):
        green_val = getGreen(px)
        setGreen(px, green_val - 150)


def moreBlue(pic):
    for px in getPixels(pic):
        blue_val = getBlue(px)
        setBlue(px, blue_val + 150)


def moreGreen(pic):
    for px in getPixels(pic):
        green_val = getGreen(px)
        setGreen(px, green_val + 150)


def darken(pic):
    for px in getPixels(pic):
        color = getColor(px)
        color = makeDarker(color)
        setColor(px, color)


def clearRed(pic):
    for px in getPixels(pic):
        setRed(px, 0)


def clearBlue(pic):
    for px in getPixels(pic):
        setBlue(px, 0)


def clearGreen(pic):
    for px in getPixels(pic):
        setGreen(px, 0)


def myColorChange(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    for px in range(randint(0, width)):
        for pix in range(randint(0, height)):
            random_color = makeColor(
                randint(0, 256), randint(0, 256), randint(0, 256))
            pixel = getPixel(pic, px, pix)
            setColor(pixel, random_color)


def blackToWhite(pic):
    whiteColor = makeColor(255, 255, 255)
    blackColor = makeColor(0, 0, 0)
    for px in getPixels(pic):
        if getRed(px) > 200:
            setColor(px, blackColor)
        else:
            setColor(px, whiteColor)


def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = raw_input(prompt)
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


while True:
    choice = raw_input("Run the program?  ")
    if choice.lower() in ('y', 'yes'):
        main()
    elif choice.lower() in ('n', 'no'):
        quit()
    else:
        continue
