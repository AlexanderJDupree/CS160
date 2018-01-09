# pixles.py


def main():
    file = pickAFile()
    image = makePicture(file)
    # show(image)
    # show_values(image)
    change_color(image)
    explore(image)


def change_color(image):
    for p in range(1, 170):
        pixel = getPixel(image, 100, p)
        new_color = makeColor(255, 0, 0)
        setColor(pixel, new_color)
    # pixel1 = getPixel(image, 100, 101)
    # pixel2 = getPixel(image, 100, 102)
    # pixel3 = getPixel(image, 100, 103)
    # new_color = makeColor(255, 0, 0)
    # setColor(pixel1, new_color)
    # setColor(pixel2, new_color)
    # setColor(pixel3, new_color)


def show_values(image):
    printNow(getWidth(image))
    printNow(getHeight(image))

    pixel = getPixel(image, 100, 80)
    printNow(pixel)
    printNow(getX(pixel))
    printNow(getY(pixel))


main()
