# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

# p1 = Person("saurav",25,"Amravati")
# print(p1.name)
# print(p1.age)
# print(p1.city)

# task 1

# class Student:
#     def __init__(self, name, age, skills = []):
#         self.name = name
#         self.age = age
#         self.skills = skills

#     def introduction(self):
#         print(f"Hi, I am {self.name} and I am {self.age} year old.")

#     def add_skills(self,new_skills):
#         return self.skills.append(new_skills)
        



# s1 = Student("Saurav", 25, ["python", "React"])
# s1.introduction()

# s1.add_skills("FastAPI")
# print("Name : ", s1.name)
# print("Age : ", s1.age)
# print("Skills : ",s1.skills)

# class Employee:
#     def __init__(self,name,salary,position):
#         self.name = name
#         self.salary = salary
#         self.position = position

#     def details(self):
#         print(f"Employeed name : {self.name} , Salary : {self.salary}, Position : {self.position}")
        
#     def increse_salary(self, amount):
#         self.salary += amount
#         print("Incresed salary : ", self.salary + amount)

# e1 = Employee("Saurav", 50000, "Developer")
# e1.increse_salary(1000)
# e1.details()

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         if amount <= 0:
#             print("Deposited amount must be posative")
#             return
#         self.balance += amount
#         print(f"Deposited: {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive!")
#             return
        
#         if amount > self.balance:
#             print("Insufficiant balance")
#         else:
#             self.balance -= amount
#             print(f"withdrew: {amount}. Remaining balance: {self.balance}")

#     def check_balance(self):
#         print("current balance:", self.balance)
#         return self.balance


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self, quantity):
        if self.stock <= 0:
            print("Insufficient stock")

        
