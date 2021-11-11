"""Task 2.
Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day
depends on the day of week. Having a pizza-of-the-day simplifies ordering for customers.
They don't have to be experts on specific types of pizza. Also, customers can add extra
ingredients to the pizza-of-the-day. Write a program that will form orders from customers.
"""
import json
from datetime import datetime


class Pizza:
    """
        class describes a pizza.
        Attributes:
        -----------
        day : str
            day of week
        name : str
            name of pizza
        ingredients : list of str
            ingredients of pizza
        price : int or float
            price of pizza
        additions : list of str
        """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        self.day = day
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.additions = additions

    @property
    def additions(self):
        return self.__additions

    @additions.setter
    def additions(self, additions):
        with open('Ingredients.json') as f:
            adds = json.load(f)
        if not all(isinstance(addition, str) for addition in additions):
            raise TypeError("Wrong type of ingredients!")
        if not set(additions).issubset(adds):
            raise ValueError("There aren't such ingredients!")
        self.__additions = additions

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name of pizza must be str!")
        if not name:
            raise ValueError("Name of pizza can't be empty!")
        self.__name = name

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Day must be str!")
        if not day:
            raise ValueError("Day can't be empty!")
        if day not in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
            raise ValueError("Wrong day of week!")
        self.__day = day

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Wrong type of ingredients!")
        self.__ingredients = ingredients

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int) and not isinstance(price, float):
            raise TypeError("Wrong type of ingredients!")
        if price <= 0:
            raise ValueError("Price must be more than 0!")
        self.__price = price

    def add_additions(self, addition):
        """
        :param addition:
            additions to add
        adds new additions to the pizza
        """
        with open('Ingredients.json') as f:
            adds = json.load(f)
        if not isinstance(addition, str):
            raise TypeError("Wrong type of addition")
        if addition not in adds:
            raise ValueError("There aren't such ingredients!")
        self.additions.append(addition)

    def del_additions(self, addition):
        """
        :param addition:
            addition to delete from pizza
        deletes addition from the pizza
        """
        if not isinstance(addition, str):
            raise TypeError("Wrong type of addition")
        if addition not in self.additions:
            raise ValueError("There aren't such additions!")
        self.additions.remove(addition)

    def __str__(self):
        if not self.additions:
            return f"Pizza of the day {self.day}, name: '{self.name}', ingredients: {self.ingredients}"
        else:
            return f"Pizza of the day {self.day}, name: '{self.name}', ingredients: {self.ingredients}, additions: {self.additions} "


class PizzaSunday(Pizza):
    """
        class describes a pizza of the Sunday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)

    def __str__(self):
        if not Pizza.additions:
            return f"Pizza of the day Sunday, name: '{Pizza.name}', ingredients: {Pizza.ingredients}"
        else:
            return f"Pizza of the day Sunday, name: '{Pizza.name}', ingredients: {Pizza.ingredients}, additions: {Pizza.additions}"


class PizzaMonday(Pizza):
    """
        class describes a pizza of the Monday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class PizzaTuesday(Pizza):
    """
        class describes a pizza of the Tuesday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class PizzaWednesday(Pizza):
    """
        class describes a pizza of the Wednesday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class PizzaThursday(Pizza):
    """
        class describes a pizza of the Thursday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class PizzaFriday(Pizza):
    """
        describes a pizza of the Friday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class PizzaSaturday(Pizza):
    """
        class describes a pizza of the Saturday.
    """
    def __init__(self, day, name, ingredients, price, additions=None):
        if additions is None:
            additions = []
        super().__init__(day, name, ingredients, price, additions)


class Order:
    """
    class describes a pizza.
    Attributes:
    -----------
    pizzas : list
        list of Pizza
    """
    def __init__(self, pizzas):
        self.pizzas = pizzas

    @property
    def pizzas(self):
        return self.__pizzas

    @pizzas.setter
    def pizzas(self, pizzas):
        if not all(isinstance(p, Pizza) for p in pizzas):
            raise TypeError("Wrong type of pizza!")
        self.__pizzas = pizzas

    def add_pizza(self, pizza):
        """
        :param pizza: pizza to add to the order
        adds pizza to the order
        """
        if not isinstance(pizza, Pizza):
            raise TypeError("Wrong type!")
        self.pizzas.append(pizza)

    def del_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Wrong type!")
        if pizza not in self.pizzas:
            raise ValueError("No such pizza in the order!")
        self.pizzas.remove(pizza)

    def get_price(self):
        """
        :return: total cost of the order
        """
        cost = 0
        with open('Ingredients.json') as f:
            added_ingredients = json.load(f)
        for pizza in self.pizzas:
            cost += pizza.price
            for adds in pizza.additions:
                cost += added_ingredients[adds]
        return cost

    def __str__(self):
        list_pizzas = ""
        for pizza in self.pizzas:
            list_pizzas += str(pizza)
            list_pizzas += '\n'
        return f"Your order: \n{list_pizzas}Price: {self.get_price()}"


def find_day_pizza(addings=None):
    """
    :param addings: addings of pizza
    :return: day of week in the file
    """
    if addings is None:
        addings = []
    with open('Pizza.json') as file_pizza:
        menu = json.load(file_pizza)
    day_week = None
    for days in menu:
        if datetime.today().strftime('%A') == days["day"]:
            day_week = days
    if not day_week:
        raise ValueError("Wrong day!")
    pizza_dict = {
        "Sunday": PizzaSunday,
        "Monday": PizzaMonday,
        "Tuesday": PizzaTuesday,
        "Wednesday": PizzaWednesday,
        'Thursday': PizzaThursday,
        "Friday": PizzaFriday,
        "Saturday": PizzaSaturday
    }
    return pizza_dict[day_week["day"]](day_week["day"], day_week["type"], day_week["ingredients"], day_week["price"], addings)


data = [{
    "day": "Sunday",
    "type": "Pepperoni",
    "ingredients": ["salami", "olives", "mozzarella", "bacon"],
    "price": 105
},  {
    "day": "Monday",
    "type": "Americana",
    "ingredients": ["salami", "ham", "mozzarella", "bacon"],
    "price": 110
  },  {
    "day": "Tuesday",
    "type": "Spicy",
    "ingredients": ["salami", "ham", "mozzarella", "bacon", "mushrooms", "pepper", "onion"],
    "price": 135
  },  {
    "day": "Wednesday",
    "type": "4 cheeses",
    "ingredients": ["mozzarella", "parmesan", "brie", "ricotta"],
    "price": 150
  },  {
    "day": "Thursday",
    "type": "Hawaiian",
    "ingredients": ["chicken", "pineapple", "mozzarella", "souse"],
    "price": 105
  },  {
    "day": "Friday",
    "type": "4 meats",
    "ingredients": ["mozzarella", "italian sausage", "pepperoni", "ham", "bacon"],
    "price": 140
  },  {
    "day": "Saturday",
    "type": "Vegan",
    "ingredients": ["tomatoes", "pepper", "broccoli", "mushrooms"],
    "price": 100
}]
adds = {
  "mushrooms": 20,
  "mozzarella": 30,
  "bacon": 35,
  "olives": 25,
  "tomatoes": 15
}

with open('Pizza.json', 'w') as out_file:
    json.dump(data, out_file, indent=4)
with open('Ingredients.json', 'w') as out_adds:
    json.dump(adds, out_adds, indent=4)
pizza1 = find_day_pizza(["mushrooms", "olives"])
pizza2 = find_day_pizza()
pizza2.add_additions("bacon")
order1 = Order([pizza1])
order1.add_pizza(pizza2)
print(order1)
