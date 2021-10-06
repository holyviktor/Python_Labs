class Product:
    def __init__(self, price, description, dimensions):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Wrong type of price!")
        elif price <= 0:
            raise ValueError("Wrong value of price!")
        else:
            self.price = price
        if not isinstance(description, str):
            raise TypeError("Wrong type of description!")
        self.description = description
        if not isinstance(dimensions, int):
            raise TypeError("Wrong type of dimensions!")
        elif dimensions <= 0:
            raise ValueError("Wrong value of dimensions!")
        self.dimensions = dimensions


class Customer:
    def __init__(self, surname, name, patronymic, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str):
            raise TypeError("Wrong type of full name!")
        elif not surname.isalpha() or not name.isalpha() or not patronymic.isalpha():
            raise ValueError("Wrong value of full name!")
        else:
            self.surname = surname
            self.name = name
            self.patronymic = patronymic
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone!")
        elif not surname.isalpha() or not name.isalpha() or not patronymic.isalpha():
            raise ValueError("Wrong value of phone!")
        else:
            self.phone = phone


class Order:
    __cost = 0

    def __init__(self, customer, *products):
        self.customer = customer
        self.products = products

    def calculating(self):
        for product in self.products:
            self.__cost += product.price

    def show_data_on_console(self):
        print("Your order:")
        print(self.customer.name, self.customer.surname)
        for product in self.products:
            print(product.description, " ", product.price)
        print("Cost is:")
        print(self.__cost)


product1 = Product(50000, "computer", 2)
product2 = Product(15000, "mobile phone", 3)
customer1 = Customer("Ivanov", "Ivan", "Petrovich", "38098989898")
order1 = Order(customer1, product1, product2)
order1.calculating()
order1.show_data_on_console()
