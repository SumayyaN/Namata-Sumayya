class Vehicle:
    def description(self):
        print("This is a  vehicle")

class Car(Vehicle):
    def description(self):
        print("This is a car")

class Bike(Vehicle):
    def description(self):
        print("This is a bike")

class Hybrid(Car, Bike):
    pass  

hybrid_vehicle = Hybrid()
hybrid_vehicle.description()  

# Checking MRO
print(Hybrid.mro())  
