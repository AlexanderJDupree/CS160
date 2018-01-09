def main():
    file = pickAFile()
    image = makePicture(file)
    image = mirror_inverse(image)
    show(image)


def mirror_right(image):
    width = getWidth(image)
    height = getHeight(image)
    for x in range(width / 2):
        for y in range(height):
            left_pixel_color = getColor(getPixel(image, x, y))
            right_pixel = getPixel(image, width - x - 1, y)
            setColor(right_pixel, left_pixel_color)
    return image


def mirror_left(image):
    width = getWidth(image)
    height = getHeight(image)
    for x in range(width / 2):
        for y in range(height):
            right_pixel_color = getColor(getPixel(image, width - x - 1, y))
            left_pixel = getPixel(image, x, y)
            setColor(left_pixel, right_pixel_color)
    return image


def mirror_top(image):
    width = getWidth(image)
    height = getHeight(image)
    for x in range(width):
        for y in range(height / 2):
            top_pixel_color = getColor(getPixel(image, x, y))
            bottom_pixel = getPixel(image, x, height - y - 1)
            setColor(bottom_pixel, top_pixel_color)
    return image


def mirror_bottom(image):
    width = getWidth(image)
    height = getHeight(image)
    for x in range(width):
        for y in range(height / 2):
            bottom_pixel_color = getColor(getPixel(image, x, height - y - 1))
            top_pixel = getPixel(image, x, y)
            setColor(top_pixel, bottom_pixel_color)
    return image


def mirror_inverse(image):
    width = getWidth(image)
    height = getHeight(image)
    x = width
    y = height
    counter = 0
    while x > 0:
        while y > 0:
            first_pixel_color = getColor(getPixel(image, x - 1, y - 1))
            pixel_inverse = getPixel(image, width - x, height - y)
            setColor(pixel_inverse, first_pixel_color)
            y -= 1
        counter += 1
        x -= 1
        y = height - counter
    # for x in range(width):
    #     for y in range(height):
    #         first_pixel_color = getColor(getPixel(image, x, y))
    #         pixel_inverse = getPixel(image, width - x - 1, height - y - 1)
    #         setColor(pixel_inverse, first_pixel_color)
    return image


main()
