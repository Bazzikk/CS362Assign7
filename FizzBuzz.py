def fizzbuzz(num):
    if (num > 0 and num <= 100):
        if (num % 5 == 0):
            if (num % 3 == 0):
                return "FizzBuzz"
            else:
                return "Buzz"
        else:
            if (num % 3 == 0):
                return "Fizz"
            else:
                return num
    else:
        return None
