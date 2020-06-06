from  import People
# marcus
# passengers should inherit from people and generate a the report
class Passengers(People):
    def __init__(self, __name, __tax_no, over_18):
        super().__init__(__name, __tax_no, over_18)