def main():
    # changePhrase()
    splice()


def splice():

    phrase = "Go Trailblazers!"

    print(phrase[5])
    print(phrase[2:])
    print(phrase[:5])
    print(phrase[-8:10])
    print(phrase[6:8])
    print(phrase[0:9:2])
    print(phrase[0::3])
    print(phrase[-1])
    print(phrase[-1:-5:-1])
    print(phrase[::-1])

    locationT = phrase.find('T')
    print("T is at cell", locationT)
    print(phrase[:locationT] + "Astros")

    print(phrase[0].isupper())


def changePhrase():

    phrase = "Python is so fun!"

    print(phrase[::-1])
    print(phrase.upper())
    print(phrase.capitalize())
    print(phrase.title())
    print(phrase.swapcase())
    print(phrase.split())

    # answer = "Yes"
    # while answer.lower() in ('yes', 'y'):
    #     print("Repeating......")
    #     answer = input("again? yes or no:  ")


main()
