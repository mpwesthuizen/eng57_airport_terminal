class People:

    def __init__(self, __name='', __tax_no='', over_18=True or False):
        self.__name = __name
        self.__tax_no = __tax_no
        self.over_18 = over_18

    def get_name(self):
        return self.__name.title()

    def get_tax_no(self):
        return self.__tax_no

    def get_over_18(self):
        return self.over_18

