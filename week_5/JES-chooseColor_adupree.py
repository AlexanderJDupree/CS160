# file: JES-chooseColor_adupree.py
# description:Create a user defined color, graph sine cosine, and unit circle
# author: Alex Dupree
# date: 10/25/2017
# compilers: JES 5.01

import math
from random import randint


def main():
    intro()
    file = pickAFile()
    image = makePicture(file)
    color_values = get_color()
    shape(color_values, image)
    show(image)


def intro():
    print("\n\tCOLOR PICKER AND SINE IMAGER")
    print("\nThis program will allow you to create a color and draw a circle "
          "with that color")
    print("\nAs well, it will draw a period of sine and cosine in random colors")


def get_color():
    colors = ["red", "green", "blue"]
    n = 0
    while n < 3:
        try:
            value = int(input("Enter %s value between 0 - 255:  " % colors[n]))
        except ValueError:
            print("ERROR: Color values must be postive integers")
        if value > 255 or value < 0:
            print("ERROR: Color values must be postive integers between 0-255")
            continue
        else:
            colors[n] = value
            n += 1
    return colors


def shape(colors, image):
    new_color = makeColor(colors[0], colors[1], colors[2])
    x_limit = getWidth(image)
    y_limit = getHeight(image)
    for x in range(x_limit):
        random_color = makeColor(
            randint(0, 256), randint(0, 256), randint(0, 256))
        y_value = int(math.sin(((2 * math.pi) / x_limit) * x)
                      * (y_limit // 3) + y_limit // 2)
        x_value = int(math.cos(((2 * math.pi) / x_limit) * x)
                      * (y_limit // 3) + y_limit // 2)
        pixel = getPixel(image, x_value, y_value)
        setColor(pixel, random_color)
        pixel2 = getPixel(image, x, y_value)
        setColor(pixel2, random_color)
        pixel3 = getPixel(image, x, x_value)
        setColor(pixel3, random_color)


main()
