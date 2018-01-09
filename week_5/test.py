def get_coords(image):
    coords = []
    n = 0
    while n < 4:
        try:
            x = int(input("Enter X Coordinate for coordinate pair %d:  " % (n + 1)))
            y = int(input("Enter Y Coordinate for coordinate pair %d:  " % (n + 1)))
        except ValueError:
            print("ERROR: Coordinates must be postive integers only")
            continue
        # Checks x, y coordinate positive and within image bounds
        if x <= 0 or y <= 0 or x > getWidth(image) or y > getHeight(image):
            print("ERROR: Coordinates must be postive integers only and "
                  "within image bounds")
            continue
        else:
            coords.append([x, y])
            n += 1
    return coords


get_coords()
