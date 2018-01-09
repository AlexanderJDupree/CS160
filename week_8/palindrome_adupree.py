# file: palindrome_adupree.py
# description: Manipulates user string
# author: Alexander DuPree
# date: 11 / 15 / 2017
# compiler: Python 3.6


def main():
    while True:
        print("Enter a string and I'll check is it is a palindrome.\n"
              "Type 'quit' to quit.")
        string = get_string("> ")
        if string.lower() == "quit":
            print("\nHave a good day!")
            quit()
        else:
            print(output(string, check_palindrome(string)))


def check_palindrome(string):
    new_string = ''.join(e for e in string if e.isalnum())
    if new_string.lower() == new_string[::-1].lower():
        return True
    else:
        return False


def get_string(prompt):
    return input(prompt)


def output(string, palindrome=False):
    if palindrome == False:
        return "\nThe string: {} is not a palindrome\n".format(string)
    else:
        return "\nThe string: {} is a palindrome! {}\n".format(string, string[::-1])


main()
