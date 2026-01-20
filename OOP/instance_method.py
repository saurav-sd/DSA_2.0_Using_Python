class Employee:
    companey = "Google"

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name, self.salary, Employee.companey)


e1 = Employee("Saurav", "500000")
e1.show_details()