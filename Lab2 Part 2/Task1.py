class Product:
    def __init__(self, price, description, dimensions):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Wrong type of price!")
        if price <= 0:
            raise ValueError("Wrong value of price!")
        if not isinstance(description, str):
            raise TypeError("Wrong type of description!")
        if not isinstance(dimensions, int):
            raise TypeError("Wrong type of dimensions!")
        if dimensions <= 0:
            raise ValueError("Wrong value of dimensions!")
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str):
            raise TypeError("Wrong type of full name!")
        if not surname.isalpha() or not name.isalpha() or not patronymic.isalpha():
            raise ValueError("Wrong value of full name!")
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone!")
        if not surname.isalpha():
            raise ValueError("Wrong value of phone!")
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}, {self.phone}"


class Order:
    def __init__(self, customer, products):
        if not isinstance(customer, Customer) or not all([isinstance(prod, Product) for prod in products]):
            raise TypeError("Wrong type of object!")
        self.customer = customer
        self.products = products

    def calculating(self):
        cost = 0
        for product in self.products:
            cost += product.price
        return cost

    def add(self, product):
        self.products.add(product)

    def delete(self, product):
        self.products.remove(product)

    def __str__(self):
        return f"Customer is: {self.customer} \nCost of order: {self.calculating()}"


product1 = Product(50000, "computer", 2)
product2 = Product(15000, "mobile phone", 3)
product3 = Product(500, "mouse", 1)
customer1 = Customer("Ivanov", "Ivan", "Petrovich", "38098989898")
order1 = Order(customer1, {product1, product2, product3})
order1.delete(product2)
print(order1)
