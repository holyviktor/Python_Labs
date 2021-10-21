import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Wrong type!")
        if not denominator:
            raise ValueError("Wrong value!")
        divider = math.gcd(numerator, denominator)
        self.__numerator = numerator/divider
        self.__denominator = denominator/divider

    def show_fraction(self):
        return str(int(self.__numerator))+"/"+str(int(self.__denominator))

    def show_value(self):
        return self.__numerator/self.__denominator


fraction = Rational(4, 8)
print(fraction.show_fraction())
print(fraction.show_value())

