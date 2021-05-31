def fizzbuzz(input):

    if (input % 3 == 0):
        if (input % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if (input % 5 == 0):
            print("Buzz")
        else:
            print(input)
