import pytest
import FizzBuzz

class TestClass:
    def test_one(self):
        assert FizzBuzz.fizzbuzz(0) == None

    def test_two(self):
        assert FizzBuzz.fizzbuzz(101) == None

    def test_three(self):
        assert FizzBuzz.fizzbuzz(1) == 1

    def test_four(self):
        assert FizzBuzz.fizzbuzz(3) == "Fizz"

    def test_five(self):
        assert FizzBuzz.fizzbuzz(5) == "Buzz"

    def test_six(self):
        assert FizzBuzz.fizzbuzz(15) == "FizzBuzz"
