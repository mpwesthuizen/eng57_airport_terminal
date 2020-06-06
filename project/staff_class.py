from .people_class import People


class Staff(People):
    def __init__(self, __name, __tax_no, over_18, job_title, company, salary_per_flight):
        super().__init__(__name, __tax_no, over_18)
        self.company = company
        self. salary_per_flight = float(salary_per_flight)
