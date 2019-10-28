def is_anagram(param1, param2):
    for letter in param1:
        if letter not in param2:
            return False
    for letter in param2:
        if letter not in param1:
            return False
    return True
