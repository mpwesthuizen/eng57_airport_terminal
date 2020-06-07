from project.people_class import *


class Staff(People):
    def __init__(self, __name, __tax_no, over_18, job_title, company, salary_per_flight):
        super().__init__(__name, __tax_no, over_18)
        self.job_title = job_title
        self.company = company
        self. salary_per_flight = float(salary_per_flight)

    def get_job_title(self):
        return self.job_title

    def get_company(self):
        return self.company

    def get_salary_gpb(self):
        flight_sal = self.salary_per_flight
        return f'£{flight_sal:0,.2f}'

staff1 = Staff('Marcus', '236547A', True, 'Trainee Devops Engineer', 'KLM', 550.00)

print(staff1.get_name())
print(staff1.get_tax_no())
print(staff1.get_over_18())
print(staff1.get_job_title())
print(staff1.get_company())
print(staff1.get_salary_gpb())