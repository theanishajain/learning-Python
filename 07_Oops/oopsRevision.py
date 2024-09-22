class Car:
        def __init__(self, brand, model):
           self.brand = brand
           self.model = model
           print("trying something new 1")

        def full_name(self):
            return self.brand +" " + self.model
        #       return f"{self.brand} {self.model}"
        
        
class ElectricCar(Car):
        def __init__(self,brand,model,battery_size):
                super().__init__(brand,model)
                self.battery_size = battery_size
                
# car = Car()                       
my_car = Car("Tata" , "Toyota")
print(my_car.full_name())