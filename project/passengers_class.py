from project.people_class import *


class Passengers(People):
    def __init__(self, __name, __tax_no, over_18, passport_no, dob, seat_type):
        super().__init__(__name, __tax_no, over_18)
        self._passport_no = passport_no
        self.dob = dob
        self.seat_type = seat_type

    def get_passport_no(self):
        return self._passport_no

    def get_dob(self):
        return self.dob

    def get_seat_type(self):
        return self.seat_type

    def set_ticket_type(self, seat_type):
        if self.over_18 is False and seat_type == 'first class'.lower() or seat_type == 'business class'.lower():
            return 'premium junior'
        elif self.over_18 is False and seat_type == 'standard'.lower():
            return 'standard junior'
        else:
            if seat_type == 'first class'.lower():
                return 'first class'
            elif seat_type == 'business class'.lower():
                return 'business class'
            elif seat_type == 'standard class'.lower():
                return 'standard class'

    def get_ticket_price(self):
        if self.set_ticket_type == 'standard class':
            s_price = 40
            return f'£{s_price}'
        elif self.set_ticket_type == 'business class':
            b_price = 60
            return f'£{b_price}'
        elif self.set_ticket_type == 'first class':
            f_price = 70
            return f'£{f_price}'
        elif self.set_ticket_type == 'junior standard':
            js_price = 30
            return f'£{js_price}'
        elif self.set_ticket_type == 'junior premium':
            jp_price = 50
            return f'£{jp_price}'

person1 = Passengers('Marcus', '236547A', True, 123454321, '01/01/2020','First class')
print(person1.get_name())
print(person1.get_tax_no())
print(person1.get_over_18())
print(person1.get_passport_no())
print(person1.dob)
print(person1.seat_type)
print(person1.set_ticket_type(person1.seat_type))
print(person1.get_ticket_price())