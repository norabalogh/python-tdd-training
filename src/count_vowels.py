def count_vowels(param):
    if type(param) is not str:
        raise Exception("Please use string as input")
    return len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], param)))
