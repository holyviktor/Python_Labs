"""Task 1.
Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event),
late ticket (purchased fewer than 10 days before the event) and student ticket.
Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the regular ticket price.
All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String.
"""
import json
from datetime import datetime, timedelta

DAYS_ADVANCE = 60
DAYS_LATE = 10
DAYS_NULL = 0
PRICE_LATE = 1.1
PRICE_ADVANCE = 0.4
PRICE_STUDENT = 0.5


class RegularTicket:
    def __init__(self, name, number, price, code, date):
        """
        class describes a regular ticket.
        Attributes:
        -----------
        name: str
            name of event
        number: str
            number of ticket
        price: float
            price of ticket
        code: int
            code of event
        date: str
            date of event
        Methods:
        --------
        get_price():
            returns price of ticket
        add():
            adds ticket to file
        type_ticket():
            returns type of ticket
        """
        self.name = name
        self.number = number
        self.price = price
        self.code = code
        self.date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        if not name:
            raise ValueError("Name can't be empty!")
        self.__name = name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            raise TypeError("Number must be str!")
        self.__number = number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError("Price must be int or float!")
        if price <= 0:
            raise ValueError("Price must be more than 0!")
        self.__price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must be int!")
        if code <= 0:
            raise ValueError("Code must be more than 0!")
        self.__code = code

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be str!")
        try:
            datetime.strptime(date, "%m/%d/%y")
        except ValueError:
            raise ValueError("Wrong date!")
        self.__date = date

    def get_price(self):
        """returns price of ticket"""
        return self.price

    def __str__(self):
        return f"Regular ticket with number {self.number}, price: {self.get_price()}"

    def type_ticket(self):
        """returns type of ticket"""
        return "Regular ticket"

    def add(self):
        """adds ticket to file"""
        with open("PurchasedTickets.json") as infile:
            bought_tickets = json.load(infile)
        for bought in bought_tickets:
            if self.number == bought["number"]:
                raise ValueError("Ticket with this number is already exists!")
        bought_tickets.append({'number': self.number, 'price': self.get_price(),
                               'type': self.type_ticket(), 'event': self.name, 'code': self.code, 'date': self.date})
        with open("PurchasedTickets.json", 'w') as writefile:
            json.dump(bought_tickets, writefile, indent=4)


class AdvanceTicket(RegularTicket):
    """
    class describes an advance ticket.
    Methods:
    --------
    get_price():
        returns price of ticket
    type_ticket():
        returns type of ticket
    """
    def __init__(self, name, number, price, code, date):
        super().__init__(name, number, price, code, date)

    def get_price(self):
        """returns price of ticket"""
        return self.price * PRICE_ADVANCE

    def __str__(self):
        return f"Advance ticket with number {self.number}, price: {self.get_price()}"

    def type_ticket(self):
        """returns type of ticket"""
        return "Advance ticket"


class StudentTicket(RegularTicket):
    """
        class describes a student ticket.
        Methods:
        --------
        get_price():
            returns price of ticket
        type_ticket():
            returns type of ticket
    """
    def __init__(self, name, number, price, code, date):
        super().__init__(name, number, price, code, date)

    def get_price(self):
        """return: price of ticket"""
        return self.price * PRICE_STUDENT

    def __str__(self):
        return f"Student ticket with number {self.number}, price: {self.get_price()}"

    def type_ticket(self):
        """returns type of ticket"""
        return "Student ticket"


class LateTicket(RegularTicket):
    """
        class describes a late ticket.
        Methods:
        --------
        get_price():
            returns price of ticket
        type_ticket():
            returns type of ticket
    """
    def __init__(self, name, number, price, code, date):
        super().__init__(name, number, price, code, date)

    def get_price(self):
        """returns price of ticket"""
        return self.price * PRICE_LATE

    def __str__(self):
        return f"Late ticket with number {self.number}, price: {self.get_price()}"

    def type_ticket(self):
        """returns type of ticket"""
        return "Late ticket"


class Order:
    """
        class describes an order of user.
        Attributes:
        -----------
        tickets: list
            all tickets in an order
        Methods:
        --------
        find_cost():
            returns cost of all tickets in order
        add():
            adds ticket to an order
    """
    def __init__(self, tickets):
        self.tickets = tickets

    def find_cost(self):
        """returns cost of all tickets in order"""
        cost = 0
        for ticket in self.tickets:
            cost += ticket.get_price()
        return cost

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        self.__tickets = tickets

    def add(self, ticket):
        """adds ticket to an order"""
        if not isinstance(ticket, RegularTicket) and not isinstance(ticket, StudentTicket) \
                and not isinstance(ticket, LateTicket) and not isinstance(ticket, AdvanceTicket):
            raise TypeError("Wrong type of ticket!")
        self.tickets.append(ticket)

    def __str__(self):
        list_tickets = ""
        for ticket in self.tickets:
            list_tickets += str(ticket)
            list_tickets += '\n'
        return f"Your order: \n{list_tickets}Total cost: {self.find_cost()}"


def find_event(name):
    """
    finds event in file by its name
    :param name: name of event
    :return: found event
    """
    with open('Event.json') as file_event:
        all_event = json.load(file_event)
    name_event = None
    for event in all_event:
        if name == event["name"]:
            name_event = event
    if not name_event:
        raise ValueError("Wrong name of event!")
    return name_event


def get_by_number(number):
    """
    finds ticket in file by number
    :param number: number of ticket to find
    :return: ticket by number
    """
    with open('PurchasedTickets.json') as file_tickets:
        purchased_tickets = json.load(file_tickets)
    name_ticket = None
    for ticket in purchased_tickets:
        if number == ticket["number"]:
            name_ticket = ticket
    if not name_ticket:
        raise ValueError("No tickets with such number!")
    dict_tickets = {
        "Regular ticket": RegularTicket,
        "Student ticket": StudentTicket,
        "Advance ticket": AdvanceTicket,
        "Late ticket": LateTicket
    }
    return \
        dict_tickets[name_ticket["type"]](name_ticket["event"], name_ticket["number"], name_ticket["price"],
                                          name_ticket["code"], name_ticket["date"])


def create_instance_ticket(number, name, student=False):
    """
    finds type of ticket and creates instance
    :param number: number of ticket
    :param name: name of event
    :param student: indicator if ticket is student
    :return: instance of ticket
    """
    event = find_event(name)
    delta = datetime.strptime(event["date"], "%d/%m/%y") - datetime.now()
    number = str(event["code"]) + '.' + str(number)
    if event["seats"] < 1:
        raise ValueError("No tickets left!")
    event["seats"] -= 1
    if timedelta(days=DAYS_NULL) > delta:
        raise ValueError("Wrong value!")
    elif student:
        ticket = StudentTicket(name, number, event["price"], event["code"], event["date"])
    elif delta >= timedelta(days=DAYS_ADVANCE):
        ticket = AdvanceTicket(name, number, event["price"], event["code"], event["date"])
    elif timedelta(days=DAYS_LATE) >= delta:
        ticket = LateTicket(name, number, event["price"], event["code"], event["date"])
    else:
        ticket = RegularTicket(name, number, event["price"], event["code"], event["date"])
    ticket.add()
    return ticket


ticket1 = create_instance_ticket(1, "Python")
ticket2 = create_instance_ticket(2, "Java", True)
order = Order([ticket1])
order.add(ticket2)
print(order)
print(get_by_number("1.1"))
