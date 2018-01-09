# loops.py


def main():
    # count_up()
    # count_down()
    # sumNum()
    # repeat_msg()
    # secret_word()
    # forHello()
    fahrToCells()


def fahrToCells():
    print("Fahr", '\t\t', "Cels")
    for i in range(0, 101, 10):
        print("{} \t\t {}".format(i, int((i - 32) * 5 / 9.0)))


def forHello():
    for x in range(5):
        print("Hello, world")
        print(x)


def count_up():
    # for n in range(5):
    #     print(n + 1)

    count = 1
    while count <= 5:
        print(count, end=" ")
        count += 1
    print("\nout of loop, count =", count)


def count_down():
    count = 10
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("\nBLAST OFF!")


def sumNum():
    how_many = int(input("how many numbers to add?  "))
    total = 0
    avg = how_many
    while how_many > 0:
        try:
            number = int(input("Enter number:  "))
        except ValueError:
            print("Error: Integers only")
        else:
            total += number
            how_many -= 1
    print("Sum of {} numbers entered: {}".format(avg, total))
    print("Average of numbers entered: {}".format(total / avg))


def repeat_msg():
    while True:
        print("Go Seahawks!")
        message = input("Do you want to see the message again? y or n \n")
        if message.lower() in ('n', 'no'):
            break
        if message.lower() in ('y', 'yes'):
            continue
        else:
            print("Error: invalid input; repeating message")
    print("Bye!")


def secret_word():
    secret = "apple"
    guess = ""
    guess_count = 0
    while guess_count < 3:
        guess = input("Enter a fruit: ")
        if guess == secret:
            print("You got it!")
            break
        print("nope! Try again.")
        guess_count += 1
        print("You took {} guess(es)".format(guess_count))
    if guess_count == 3:
        print("You took too many guesses")


main()
