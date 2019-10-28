from datetime import datetime, date


def agecalc(param):
    today = date.today()
    date_of_birth = datetime.strptime(param, "%Y %m %d")
    return today.year - date_of_birth.year - (
        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
