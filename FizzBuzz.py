def fizzbuzz():
    num = 1
    while num <= 100:
        if (num > 0 and num <= 100):
            if (num % 5 == 0):
                if (num % 3 == 0):
                    print ("FizzBuzz")
                else:
                    print ("Buzz")
            else:
                if (num % 3 == 0):
                    print ("Fizz")
                else:
                    print (num)
        num = num + 1
        #else:
            #return None
fizzbuzz()
