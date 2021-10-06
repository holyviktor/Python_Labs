import math


class Rational:

    def __init__(self, __numerator=5, __denominator=8):
        if not isinstance(__numerator, int) or not isinstance(__denominator, int):
            raise TypeError("Wrong type!")
        elif not __denominator:
            raise ValueError("Wrong value!")
        else:
            divider = math.gcd(__numerator, __denominator)
            self.__numerator = __numerator/divider
            self.__denominator = __denominator/divider

    def show_fraction(self):
        return str(int(self.__numerator))+"/"+str(int(self.__denominator))

    def show_value(self):
        return self.__numerator/self.__denominator


fraction = Rational(9, 8.6)
print(fraction.show_fraction())
print(fraction.show_value())

