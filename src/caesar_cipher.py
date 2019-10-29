def encrpyt(text):
    result = ""
    for char in text:
        if not char.isalpha():
            result += char
        elif (char.isupper()):
            result += chr((ord(char) + 3 - 65) % 26 + 65)
        else:
            result += chr((ord(char) + 3 - 97) % 26 + 97)
    return result


def decrypt(text):
    result = ""
    print(text)
    for char in text:
        if not char.isalpha():
            result += char
        elif (char.isupper()):
            result += chr((ord(char) - 3 - 65) % 26 + 65)
        else:
            result += chr((ord(char) - 3 - 97) % 26 + 97)
    return result
