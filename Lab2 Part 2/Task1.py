class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Wrong type of price!")
        if price <= 0:
            raise ValueError("Wrong value of price!")
        self.__price = price

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Wrong type of description!")
        if not description:
            raise ValueError("Wrong value of description!")
        self.__description = description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, int):
            raise TypeError("Wrong type of dimensions!")
        if dimensions <= 0:
            raise ValueError("Wrong value of dimensions!")
        self.__dimensions = dimensions


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}, {self.phone}"

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Wrong type of surname!")
        if not surname.isalpha():
            raise ValueError("Wrong value of surname!")
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type of name!")
        if not name.isalpha():
            raise ValueError("Wrong value of name!")
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Wrong type of patronymic!")
        if not patronymic.isalpha():
            raise ValueError("Wrong value of patronymic!")
        self.__patronymic = patronymic

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone!")
        if phone.isalpha():
            raise ValueError("Wrong value of phone!")
        self.__phone = phone


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if not all([isinstance(prod, Product) for prod in products]):
            raise TypeError("Wrong type of products!")
        self.__products = products

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Wrong type of customer!")
        self.__customer = customer

    def calculating(self):
        cost = 0
        for product in self.products:
            cost += product.price
        return cost

    def add(self, product):
        if not product:
            ValueError("Wrong value of data!")
        if not isinstance(product, Product):
            TypeError("Wrong type of product!")
        self.products.add(product)

    def delete(self, product):
        if not product:
            ValueError("Wrong value of data!")
        if not isinstance(product, Product):
            TypeError("Wrong type of product!")
        self.products.remove(product)

    def __str__(self):
        return f"Customer is: {self.customer} \nCost of order: {self.calculating()}"


product1 = Product(50000, "computer", 2)
product2 = Product(15000, "mobile phone", 3)
product3 = Product(500, "mouse", 1)
customer1 = Customer("Ivanov", "Ivan", "Petrovich", "38098989898")
order1 = Order(customer1, {product1, product2})
order1.add(product3)
order1.delete(product2)
print(order1)
