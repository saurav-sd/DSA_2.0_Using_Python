from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    def receipt(self):
        print("Payment completed")

class CreditCard(Payment):
    def pay(self, amount):
        return amount

class UPI(Payment):
    def pay(self, amount):
        return amount