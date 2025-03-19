# class Test:
#     x = 10

#     def f():
#         print("function")
#     f()

# t1 = Test()

# class Test:
#     x = 10

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# # Instance object menthod
#     def show(self):
#         print(self.a,self.b)

# # class object method
#     @classmethod
#     def f2(cls):
#         print(cls.x)

#     @staticmethod
#     def f3():
#         pass

# t1 = Test(1,2)
# t2 = Test(3,4)
# t1.show()
# t2.show()
# Test.f2()

class Employee:
    def __init__(self,eid,name,salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def show(self):
        print(self.eid,self.name,self.salary)

e1 = Employee(101,"Ramesh",20000)
e1.show()
