from random import randint
from project.people_class import *

class Passengers(People):
    def __init__(self, __name, __tax_no, over_18, passport_no, dob, ticket_type=None, ticket_price=None,
                 boarding_pass=None):
        super().__init__(__name, __tax_no, over_18)
        self.boarding_pass = boarding_pass
        self._passport_no = passport_no
        self.dob = dob
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price

    def purchase_ticket(self, ticket_type):
        if ticket_type == "First":
            self.ticket_type = "First"
            self.ticket_price = 1000
            self.set_boarding_pass()

        elif ticket_type == "Business":
            self.ticket_type = 'Business'
            self.ticket_price = 500
            self.set_boarding_pass()

        elif ticket_type == "Infant":
            self.ticket_type = "Infant"
            self.ticket_price = 0
            self.set_boarding_pass()

        elif ticket_type == "Economy":
            self.ticket_type = "Economy"
            self.ticket_price = 300
            self.set_boarding_pass()

    def get_boarding_pass(self):
        return self.boarding_pass

    def set_boarding_pass(self):
        if self.ticket_type == "First":
            new_bp = "BA-1", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)

        elif self.ticket_type == "Infant":
            new_bp = "BA-9", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)

        elif self.ticket_type == "Business":
            new_bp = "BA-2", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)

        elif self.ticket_type == "Economy":
            new_bp = "BA-2", str(randint(99, 999)), "-", str(randint(999, 9999))
            self.boarding_pass = ''.join(new_bp)

    def get_passport_no(self):
        return self.passport_no

    def set_passport_no(self, new_passport_no):
        self.passport_no = new_passport_no
        name = self.get_name()
        return f"Passport number updated for passenger:   {name}\n New number:   {self.passport_no}"

    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, new_ticket):
        self.ticket_type = new_ticket
        name = self.get_name()
        return f"Ticket type updated for passenger: {name}, to {self.ticket_type}"

    def passenger_details(self):
        report = vars(self)
        for key, value in report.items():
            return key.capitalize(), ": ", value


person1 = Passengers('Marcus', '236547A', True, 123454321, '01/01/2020','First class')
print(person1.get_name())
print(person1.get_tax_no())
print(person1.get_over_18())
print(person1.get_passport_no)
print(person1.dob)
print(person1.get_ticket_type())
print(person1.get_boarding_pass())