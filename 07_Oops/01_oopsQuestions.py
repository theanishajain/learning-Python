# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self,brand, model):
        print("trying something new 1")
        self.__brand = brand
        self.model = model
        print("trying something new 2")
        # Que2. 2. Class Method and Self
        # Problem: Add a method to the Car class that displays the full name of the car (brand and model).
        
        
    # def display(self):
    #     print(self.brand)
    #     print(self.model)
    
    def full_name(self):
        return f"{self.__brand} {self.model}" # by using formatted string
    
    def fuel_type(self):
        return "Diesel Or Petrol"
    
    # QUE.3 3. Inheritance
    # Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute 
    # battery_size.
class ElectricCar(Car):
        def __init__(self, brand, model, battery_size):
          super().__init__(brand, model)
          self.battery_size = battery_size
          
        def fuel_type(self):
            return "Electricity"
        


my_car = Car("Toyota", "Carolla")
# print(my_car.brand)
print(my_car.full_name())
print(my_car.fuel_type())

# Que2. 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

my_Electric_Car = ElectricCar("Tesla", "S", "653KWH")
print(my_Electric_Car.fuel_type())