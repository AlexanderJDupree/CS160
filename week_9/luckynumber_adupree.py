# file: luckynumber_adupree.py
# description: number guessing game
# authors: Alex DuPree
# date: 11/20/2017
# compiler: Python 3.6


from random import randint


def main():
    intro()
    victory, guess = guess_loop()
    message(victory, guess)


def intro():
    print("\tGUESS THE LUCKY NUMBER"
          "\nYou will heave 15 tries to guess a number between 1 - 100")


def guess_loop():
    guesses = 15
    lucky_number = randint(1, 100)

    while guesses > 0:
        try:
            guess = int(input("\nEnter a guess:  "))
        except ValueError:
            print("Error: input must be a number between 1 - 100")
            continue
        if guess > lucky_number and guess < 101:
            print("Too high")
            guesses -= 1
        elif guess < lucky_number and guess > 0:
            print("Too low")
            guesses -= 1
        elif guess == lucky_number:
            return True, guesses
        else:
            print("\nError: input must be a number between 1 - 100")
    return False, lucky_number


def message(victory, guess):
    if victory == True:
        print("Hooray you got it!\nYou took {} guess(es).\nYou're good!"
              .format(16 - guess))
    else:
        print("Sorry, you're out of guesses. The number was {}".format(guess))


main()
