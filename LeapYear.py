# To verify if a year is a leap year
def leapYearVerifier (year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
        else:
            return True
