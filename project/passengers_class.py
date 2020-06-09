from project.people_class import *


class Passengers(People):
    def __init__(self, __name, __tax_no, passport_no):
        super().__init__(__name, __tax_no)
        self._passport_no = passport_no

    def set_passport_no(self, new_passport_no):
        self.passport_no = new_passport_no
        name = self.get_name()
        return f"Passport number updated for passenger:   {name}\n New number:   {self.passport_no}"

