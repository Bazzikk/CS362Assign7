import pytest
import FizzBuzz

class TestClass:
    def test_one(self):
        assert FizzBuzz.fizzbuzz(0) == None

    def test_two(self):
        assert FizzBuzz.fizzbuzz(101) == None

    def test_three(self):
        assert FizzBuzz.fizzbuzz(1) == 1
