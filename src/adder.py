def add(num1, num2):
    """A function that adds two numbers."""
    if(type(num1) == str or type(num2) == str):
        raise Exception("Input is sting. It should be int, double.")
    return num1 + num2
