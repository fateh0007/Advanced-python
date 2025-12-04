class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def full_name(self):
        print(self.__brand + " " + self.model)
        
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla","Model S",100)
my_tesla.full_name()
        
myCar = Car("Toyota","Corolla")
myCar.full_name()
print(myCar.brand)