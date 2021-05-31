def fizzbuzz(num):
    if (num > 0 and num <= 100):
        if (num % 3 == 0):
            if (num % 5 == 0):
                return "FizzBuzz"
            else:
                return "Fizz"
        else:
            if (num % 5 == 0):
                return "Buzz"
            else:
                return num
    else:
        return None
