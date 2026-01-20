class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        print(cls.company)


Employee.change_company("Amazon")
