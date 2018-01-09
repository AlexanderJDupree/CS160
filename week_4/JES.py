# def viewPicture():
#     file = pickAFile()
#     pict = makePicture(file)
#     pixel = getPixel(pict, 0, 0)
#     pixels = getPixels(pict)
#     print("width is", getWidth(pict), "height is", getHeight(pict))
#     print("The value of the pixel at 0, 0 is: ", pixel)
#     print("A different way to get the pixel at 0, 0 is: ", pixels[0])
#     explore(pict)


# viewPicture()

# program 16, page 69
def negative(picture):
    for px in getPixels(picture):
        red = getRed(px)
        green = getGreen(px)
        blue = getBlue(px)
        negColor = makeColor(red - red, green - green, blue - blue)
        setColor(px, negColor)
    show(picture)
    repaint(picture)


file = pickAFile()
pict = makePicture(file)
negative(pict)
