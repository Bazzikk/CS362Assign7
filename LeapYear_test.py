import pytest
import LeapYear

class TestClass:
    def test_one(self):
        assert LeapYear.leapYearVerifier(4) == True

    def test_two(self):
        assert LeapYear.leapYearVerifier(100) == False

    def test_three(self):
        assert LeapYear.leapYearVerifier(400) == True
