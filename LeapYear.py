# To verify if a year is a leap year
def leapYearVerifier (year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            return False
        else:
            return True
