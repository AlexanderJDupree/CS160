# file: imagemanip1.py


def main():
    file = get_file()
    image = make_image(file)
    # more_red(image)\
    # make_sunset(image)
    # lighten(image)
    # whiteToBlack(image)
    negative(image)
    show_image(image)


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


# def more_red(image):
#     for px in getPixels(image):
#         red_val = getRed(px)
#         setRed(px, red_val + 150)

# def lighten(image):
#     for px in getPixels(image):
#         color = getColor(px)
#         color = makeLighter(color)
#         setColor(px, color)


# def whiteToBlack(image):
#     whiteColor = makeColor(255, 255, 255)
#     blackColor = makeColor(0, 0, 0)
#     for px in getPixels(image):
#         if getRed(px) > 100 and getBlue(px) < 200:
#             setColor(px, blackColor)
#         else:
#             setColor(px, whiteColor)


def negative(picture):
    for px in getPixels(picture):
        red = getRed(px)
        green = getGreen(px)
        blue = getBlue(px)
        negColor = makeColor(255 - red, 255 - green, 255 - blue)
        setColor(px, negColor)


main()
