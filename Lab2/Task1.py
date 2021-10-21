class Rectangle:

    def __init__(self, length=5.5, width=5.5):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("Wrong type!")
        if not 20.0 > length > 0.0 or not 20.0 > width > 0.0:
            raise ValueError("Wrong value!")
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def find_perimeter(self):
        return 2*(self.length + self.width)

    def find_area(self):
        return self.length * self.width


rect1 = Rectangle(7.5, 6.7)
print("a = ", str(rect1.get_length()), ",    b = " + str(rect1.get_width()))
print("perimeter is ", str(rect1.find_perimeter()), ",    area is ", str(rect1.find_area()))
