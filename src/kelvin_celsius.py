def kelvin_to_celsius(kelvin):
    if type(kelvin) is not int and type(kelvin) is not float:
        raise Exception("Please use number as an input")
    if kelvin < 0:
        raise Exception("That might be too cold")

    return float(kelvin-273.15)


def celsius_to_kelvin(celsius):
    if type(celsius) is not int and type(celsius) is not float:
        raise Exception("Please use number as an input")
    if celsius < -273.15:
        raise Exception("That might be too cold")
    return celsius+273.15
