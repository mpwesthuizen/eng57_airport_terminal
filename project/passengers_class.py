from .people_class import People
# marcus
# passengers should inherit from people and generate a the report


class Passengers(People):
    def __init__(self, __name, __tax_no, over_18, passport_no, dob, ticket_type, ticket_price):
        super().__init__(__name, __tax_no, over_18)
        self._passport_no = passport_no
        self.dob = dob
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price

    def get_passport_no(self):
        return self._passport_no

    def get_dob(self):
        return self.dob

    def set_ticket_type(self, ticket_type):
        if self.over_18 is False and ticket_type == 'first class'.lower() or ticket_type == 'business class'.lower():
            return 'premium junior'
        elif self.over_18 is False and ticket_type == 'standard'.lower():
            return 'standard junior'
        else:
            if ticket_type == 'first class'.lower():
                return 'first class'
            elif ticket_type == 'business class'.lower():
                return 'first class'
            elif ticket_type == 'standard class'.lower():
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

