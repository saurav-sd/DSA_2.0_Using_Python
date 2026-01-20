# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# print(MathUtils.add(10, 20))


# practice problem

class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, self.age,Student.school_name)

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    @staticmethod
    def is_adult(age):
        return age >= 18
        

s1 = Student("Saurav", 25)
s1.show_details()

Student.change_school("XYZ School")
s1.show_details()

print(Student.is_adult(17))
