from string import ascii_lowercase


def alphabeticShift(inputString):
    shift = []
    for c in inputString:
        try:
            shift.append(ascii_lowercase[ascii_lowercase.find(c) + 1])
        except IndexError:
            shift.append('a')

    return ''.join(e for e in shift)


def better_alphabeticShift(inputString):
    return "".join([chr(ord(i) + 1) if i != "z" else "a" for i in inputString])


def even_better_alphabeticShift(s):
    return "".join(chr((ord(i) - 96) % 26 + 97) for i in s)

# chr returns a character based on a number
# ord returns a number based on a character
