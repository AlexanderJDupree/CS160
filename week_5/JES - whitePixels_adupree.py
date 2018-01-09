# file: JES- whitePixels_adupree.py
# description:ask for four x, y coordinates and will change them to the color white
# author: Alex Dupree, Ryan Welch
# date: 10/25/2017
# compilers: JES 5.01


def main():
    intro()
    file = pickAFile()
    image = makePicture(file)
    coords = get_coords(image)
    change_color(coords, image)
    show(image)


def intro():
    print("\n\tTURN FOUR PIXELS WHITE PROGRAM\n")
    print("This program will ask for four X, Y coordinates and will change them"
          " to the color white")


def get_coords(image):
    coords = []

    try:
        x_limit = getWidth(image)
        y_limit = getHeight(image)
    except java.lang.NullPointerException:
        print("Error: Wrong file type")
        exit()

    print("Enter values between 0 and %d for X  and 0 and %d for Y"
          % (x_limit, y_limit))

    n = 0
    while n < 4:
        try:
            x = int(input("Enter X Coordinate for coordinate pair %d:  " % (n + 1)))
            y = int(input("Enter Y Coordinate for coordinate pair %d:  " % (n + 1)))
        except ValueError:
            print("ERROR: Coordinates must be postive integers only")
        # Checks x, y coordinate positive and within image bounds
        if x < 0 or y < 0 or x > x_limit or y > y_limit:
            print("ERROR: Coordinates must be postive integers only and "
                  "within image bounds")
            continue
        else:
            coords.append([x, y])
            n += 1
    return coords


def change_color(coords, image):
    new_color = makeColor(255, 255, 255)
    for x in coords:
        for y in x:
            pixel = getPixel(image, x[0], y)
            setColor(pixel, new_color)


main()
