"""
1. Modify the class Rational of Lab No2 to perform the following tasks:
- adding two Rational numbers. The result should be stored in reduced form;
- subtracting two Rational numbers. The result should be stored in reduced form;
- multiplying two Rational numbers. The result should be stored in reduced form;
- dividing two Rational numbers. The result should be stored in reduced form;
- comparison two Rational numbers.
"""

import math


class Rational:
    """
    class describes a rational fraction
    Attributes:
    ----------
    numerator : int
        numerator of the fraction
    denominator: int
        denominator of the fraction
    """
    def __init__(self, numerator=1, denominator=1):
        divider = math.gcd(numerator, denominator)
        self.__numerator = numerator//divider
        self.__denominator = denominator//divider

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("Wrong type!")
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError("Wrong type!")
        if not denominator:
            raise ValueError("Wrong value!")
        self.__denominator = denominator

    def show_fraction(self):
        return str(int(self.__numerator))+"/"+str(int(self.__denominator))

    def show_value(self):
        return self.__numerator/self.__denominator

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        numerator_new = self.numerator * other.denominator + other.numerator * self.denominator
        denominator_new = self.denominator * other.denominator
        return Rational(numerator_new, denominator_new)

    def __iadd__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator*other.denominator
        divider = math.gcd(self.numerator, self.denominator)
        self.numerator //= divider
        self.denominator //= divider
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        numerator_new = self.numerator * other.denominator - other.numerator * self.denominator
        denominator_new = self.denominator * other.denominator
        return Rational(numerator_new, denominator_new)

    def __isub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        divider = math.gcd(self.numerator, self.denominator)
        self.numerator //= divider
        self.denominator //= divider
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        numerator_new = self.numerator * other.numerator
        denominator_new = self.denominator * other.denominator
        return Rational(numerator_new, denominator_new)

    def __imul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        divider = math.gcd(self.numerator, self.denominator)
        self.numerator //= divider
        self.denominator //= divider
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        if not other.numerator:
            raise ValueError("Division by zero!")
        numerator_new = self.numerator * other.denominator
        denominator_new = self.denominator * other.numerator
        return Rational(numerator_new, denominator_new)

    def __itruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Wrong type!")
        if not other.numerator:
            raise ValueError("Division by zero!")
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        divider = math.gcd(self.numerator, self.denominator)
        self.numerator //= divider
        self.denominator //= divider
        return self

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Wrong type!")
        return (self.numerator, self.denominator) == (other.numerator, other.denominator)

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Wrong type!")
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 < numerator2

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Wrong type!")
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 <= numerator2

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Wrong type!")
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 > numerator2

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Wrong type!")
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 >= numerator2


fraction1 = Rational(4, 8)
fraction2 = Rational(5, 8)

fraction3 = fraction1 + fraction2
print(fraction3.show_fraction())
print(fraction3.show_value())

if fraction1 < fraction2:
    print("fraction1<fraction2")

fraction1 *= fraction2
print(fraction1.show_fraction())
print(fraction1.show_value())


