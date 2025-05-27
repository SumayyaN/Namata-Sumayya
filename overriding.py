class Person:
    def description(self):
        print("This is a person")

class Student(Person):
    def description(self):  
        print("This is a student")

s = Student()
s.description()  
