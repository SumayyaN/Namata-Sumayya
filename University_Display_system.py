# Base Class
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}")


# Subclass: Student
class Student(Person):
    def __init__(self, name, age, id_number, course):
        super().__init__(name, age, id_number)
        self.course = course

    def display_info(self):
        super().display_info()
        print("Role: Student")

    def enroll(self):
        print(f"{self.name} has enrolled in {self.course}.")


# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, id_number, department):
        super().__init__(name, age, id_number)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Role: Lecturer")

    def teach(self):
        print(f"{self.name} is teaching in the {self.department} department.")


# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, id_number, position):
        super().__init__(name, age, id_number)
        self.position = position

    def display_info(self):
        super().display_info()
        print("Role: Staff ")

    def work(self):
        print(f"{self.name} is working as a {self.position}.")


# Create objects
student = Student("Sumayya", 21, "ST1234", "Computer Science")
lecturer = Lecturer("Dr. Namata", 40, "LC5678", "Engineering")
staff = Staff("James", 35, "STF9876", "Administrator")

# Demonstrate behavior
print("\n--- Student Info ---")
student.display_info()
student.enroll()

print("\n--- Lecturer Info ---")
lecturer.display_info()
lecturer.teach()

print("\n--- Staff Info ---")
staff.display_info()
staff.work()
