# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
    
#     def start(self):
#         print("Vehicle started")


# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def start(self):
#         super().start()
#         print("Car started")

# c = Car("BMW", "X5")
# c.start()


class Calculator:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


calc = Calculator()
print(calc.multiply(2,3))
print(calc.multiply(2,3,4,5,6))