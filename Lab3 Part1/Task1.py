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


class RegularTicket:
    def __init__(self, number, price):
        self.number = number
        self.price = price

    def get_price(self):
        return self.price

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

    def __str__(self):
        return f"Regular ticket with number {self.number}, price: {self.price}"


class AdvanceTicket(RegularTicket):
    def __init__(self, number, price):
        super().__init__(number, price * 0.4)

    def __str__(self):
        return f"Advance ticket with number {self.number}, price: {self.price}"


class StudentTicket(RegularTicket):
    def __init__(self, number, price):
        super().__init__(number, price * 0.5)

    def __str__(self):
        return f"Student ticket with number {self.number}, price: {self.price}"


class LateTicket(RegularTicket):
    def __init__(self, number, price):
        super().__init__(number, price * 1.1)

    def __str__(self):
        return f"Late ticket with number {self.number}, price: {self.price}"


class Event:
    def __init__(self, date, regular_tickets, advance_tickets, student_tickets, late_tickets):
        self.date = date
        self.regular_tickets = regular_tickets
        self.advance_tickets = advance_tickets
        self.student_tickets = student_tickets
        self.late_tickets = late_tickets
        self.tickets = []
        self.numbers = []

    def add(self, ticket):
        if ticket.number in self.numbers:
            raise ValueError("Ticket with this number is already exists!")
        self.numbers.append(ticket.number)
        if isinstance(ticket, LateTicket):
            if self.late_tickets < 1:
                raise ValueError("No late tickets!")
            self.late_tickets -= 1
        elif isinstance(ticket, StudentTicket):
            if self.student_tickets < 1:
                raise ValueError("No student tickets!")
            self.student_tickets -= 1
        elif isinstance(ticket, AdvanceTicket):
            if self.advance_tickets < 1:
                raise ValueError("No advance tickets!")
            self.advance_tickets -= 1
        else:
            if self.regular_tickets < 1:
                raise ValueError("No regular tickets!")
            self.student_tickets -= 1
        with open("PurchasedTickets.json") as infile:
             bought_tickets = json.load(infile)
        #print(bought_tickets)
        #print(ticket)
        ticket_info = str(ticket.number) + str(ticket.price)
        bought_tickets["number"].append(ticket.number)
        with open("PurchasedTickets.json") as writefile:
            json.dump(bought_tickets, writefile, indent=4)
        self.tickets.append(ticket)

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

    @property
    def regular_tickets(self):
        return self.__regular_tickets

    @regular_tickets.setter
    def regular_tickets(self, regular_tickets):
        if not isinstance(regular_tickets, int):
            raise TypeError("Number of regular tickets must be int!")
        if regular_tickets <= 0:
            raise ValueError("Number of regular tickets must be more than 0!")
        self.__regular_tickets = regular_tickets

    @property
    def advance_tickets(self):
        return self.__advance_tickets

    @advance_tickets.setter
    def advance_tickets(self, advance_tickets):
        if not isinstance(advance_tickets, int):
            raise TypeError("Number of advance tickets must be int!")
        if advance_tickets <= 0:
            raise ValueError("Number of advance tickets must be more than 0!")
        self.__advance_tickets = advance_tickets

    @property
    def student_tickets(self):
        return self.__student_tickets

    @student_tickets.setter
    def student_tickets(self, student_tickets):
        if not isinstance(student_tickets, int):
            raise TypeError("Number of student tickets must be int!")
        if student_tickets <= 0:
            raise ValueError("Number of student tickets must be more than 0!")
        self.__student_tickets = student_tickets

    @property
    def late_tickets(self):
        return self.__late_tickets

    @late_tickets.setter
    def late_tickets(self, late_tickets):
        if not isinstance(late_tickets, int):
            raise TypeError("Number of late tickets must be int!")
        if late_tickets <= 0:
            raise ValueError("Number of student tickets must be more than 0!")
        self.__late_tickets = late_tickets


class Order:
    def __init__(self, tickets):
        self.tickets = tickets

    def find_cost(self):
        cost = 0
        for ticket in self.tickets:
            cost += ticket.price
        return cost

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        self.__tickets = tickets

    def __str__(self):
        list_tickets = ""
        for ticket in self.tickets:
            list_tickets += str(ticket)
            list_tickets += '\n'
        return f"Your order: \n{list_tickets}Total cost: {self.find_cost()}"


def create_instance(number, price, event, student=False):
    delta = datetime.strptime(event.date, "%d/%m/%y") - datetime.now()
    if timedelta(days=0) > delta:
        raise ValueError("Wrong value!")
    elif student:
        ticket = StudentTicket(number, price)
    elif delta >= timedelta(days=60):
        ticket = AdvanceTicket(number, price)
    elif timedelta(days=10) >= delta:
        ticket = LateTicket(number, price)
    else:
        ticket = RegularTicket(number, price)
    event.add(ticket)
    return ticket


with open('Event.json') as file:
    data = json.load(file)
event1 = \
    Event(data["date"], data["regular_tickets"], data["advance_tickets"], data["student_tickets"], data["late_tickets"])
ticket1 = create_instance("1234", data["price"], event1)
ticket2 = create_instance("3456", data["price"], event1, True)
order = Order({ticket1, ticket2})
print("Price of ticket is", ticket1.get_price())
print(order)
#забрати
"""
def create_instance(number, price, date):
    if not isinstance(number, str):
        raise TypeError("Number must be string!")
    if number[0] == '1':
        return RegularTicket(number, price, date)
    if number[0] == '2':
        return AdvanceTicket(number, price, date)
    if number[0] == '3':
        return StudentTicket(number, price, date)
    if number[0] == '4':
        return LateTicket(number, price, date)
    raise ValueError("Wrong value of ticket!")
"""
