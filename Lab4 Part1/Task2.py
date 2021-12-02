"""
Create a class COMPOSITION with the names of goods, their quantity and price. Define methods
for working with these data fields and overload operations to replenish product information,
retrieve product information, generate a report on the availability of goods in stock according
to the request.
"""


class Composition:
    """
        class describes a product
        Attributes:
        ----------
        name : str
            name of a product
        quantity: int
            quantity of products
        price: float
            price of product
    """
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        if not name:
            raise ValueError("Name can't be empty")
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be int!")
        if quantity <= 0:
            raise ValueError("Quantity must be more than 0!")
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Price must be int or float!")
        if price <= 0:
            raise ValueError("Price must be more than 0!")
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.quantity}, {self.price}"

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("Wrong type!")
        if other <= 0:
            raise ValueError("Wrong value")
        self.quantity += other
        return self

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Wrong type!")
        if other <= 0:
            raise ValueError("Wrong value")
        self.quantity -= other
        return self


class Goods:
    def __init__(self, goods):
        self.goods = goods

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, goods):
        if not all((good, Composition) for good in goods):
            raise TypeError("Wrong type of goods!")
        if not goods:
            raise ValueError("Goods can't be empty!")
        self.__goods = goods

    def __iadd__(self, other):
        if not isinstance(other, Composition):
            raise TypeError("Wrong type!")
        self.goods.append(other)
        return self

    def __isub__(self, other):
        if other not in self.goods:
            raise ValueError("No such composition")
        self.goods.remove(other)
        return self

    def count_cost(self):
        cost = 0
        for good in self.goods:
            cost += good.price
        return cost

    def __str__(self):
        result = ''
        for good in self.goods:
            result += str(good) + '\n'
        result += "Total cost: " + str(self.count_cost())
        return result


comp1 = Composition("Goods1", 6, 50)
comp2 = Composition("Goods2", 4, 100)
comp3 = Composition("Goods3", 3, 200)
comp3 -= 1
goods1 = Goods([comp1])
goods1 += comp2
goods1 += comp3
goods1 -= comp1
goods1.count_cost()
print(goods1)
