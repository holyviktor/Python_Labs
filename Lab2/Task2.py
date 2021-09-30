import math


class Rational:

    def __init__(self, __numerator=5, __denominator=8):
        if not __denominator:
            #print("Division by zero!")
            exit(1)
        elif not isinstance(__numerator, int) or not isinstance(__denominator, int):
            #print("Wrong type! The type must be int.")
            exit(1)
        else:
            divider = math.gcd(__numerator, __denominator)
            self.__numerator = __numerator/divider
            self.__denominator = __denominator/divider

    def show_fraction(self):
        return str(int(self.__numerator))+"/"+str(int(self.__denominator))

    def show_value(self):
        return self.__numerator/self.__denominator


fraction = Rational(2, 8)
print(fraction.show_fraction())
print(fraction.show_value())

