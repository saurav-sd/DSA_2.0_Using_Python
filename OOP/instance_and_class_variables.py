class Car:
    wheels = 4
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


c1 = Car("BMW", 500000)
c2 = Car("Audi", 600000)

print(f"Brand : {c1.brand}, Price : {c1.price} and Wheels : {c1.wheels}")
print(f"Brand : {c2.brand}, Price : {c2.price} and Wheels : {c2.wheels}")