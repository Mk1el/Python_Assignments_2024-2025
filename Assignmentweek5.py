class SmartPhone:
    def __init__(self,brand,model,os,storage):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}from {self.model}")

    def send_message(self, number, message):
        print(f"Sending message to {number}:{message}")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model}")

class SmartPhoneWithCamera(SmartPhone):
    def __init__(self, brand, model, os, storage, camera_resolution):
       super().__init__(brand, model, os, storage)
       self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} camera...")
    
# Creating an object of Smartphone class
phone1 = SmartPhone("Samsung", "Galaxy S21", "Android", "128GB")
phone1.make_call("0712345678")
phone1.send_message("0712345678", "Hello!")

# Base class Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden in derived classes

# Subclass Car that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass Boat that inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create objects of each vehicle type
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()  # The move method behaves differently for each class
