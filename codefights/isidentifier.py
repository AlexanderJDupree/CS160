import string


def variableName(name):
    invalid_chars = string.punctuation.replace("_", " ")
    if any(char in invalid_chars for char in name) or name[0].isdigit():
        return False
    else:
        return True


name = " variable"
print(variableName(name))
