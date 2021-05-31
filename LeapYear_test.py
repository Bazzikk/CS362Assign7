import pytest
import LeapYear

class TestClass:
    def test_one(self):
        assert LeapYear.leapYearVerifier(4) == True
