## Basic Class and Object
## => Create a Car class with attributes like brand and model. Then create an instance of this class
## => Add a method to the car class that displays the full name of the car (brand and model).

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.brand}, {self.model}"
    
    
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())









## Inheritance
## => Create an ElectricCar class that inherits from the car and has an additional attribute battery_size.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.brand}, {self.model}"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
    
    
# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.model)
# print(my_tesla.brand)
# print(my_tesla.full_name())








## Encapsulation
## => Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
        
#     def get_brand(self):
#         return self.__brand + "!"
    
#     def set_brand(self, brand):
#         self.__brand = brand
        
#     def full_name(self):
#         return f"{self.__brand}, {self.model}"
        
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#       return "Electric charge"
      


# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# my_tesla.set_brand("Tata")
# # print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.__dict__)









## Polymorphism
## => Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.


# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
        
#     # def get_brand(self):
#     #     return self.__brand + "!"
    
#     # def set_brand(self, brand):
#     #     self.__brand = brand
        
#     @property
#     def car_brand(self):
#         return self.__brand + "!"

#     @car_brand.setter
#     def car_brand(self, brand):
#         self.__brand = brand
        
#     def full_name(self):
#         return f"{self.__brand}, {self.model}"
        
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#       return "Electric charge"
      

# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.car_brand)
# print(my_tesla.model)
# print(my_tesla.fuel_type())









## Class Variables
## => Add a class variable to Car that keeps track of the number of cars created.


# class Car:
    
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1

#     @property
#     def car_brand(self):
#         return self.__brand + "!"

#     @car_brand.setter
#     def car_brand(self, brand):
#         self.__brand = brand
        
#     def full_name(self):
#         return f"{self.__brand}, {self.model}"
        
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#       return "Electric charge"
      

# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.car_brand)

# safari = Car("Tata", "Safari")
# Nexon = Car("Tata", "Nexon")

# print(Car.total_car)








## Static Method
## => Add a static method to the Car class that returns a general description of a car.


# class Car:
    
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1

#     @property
#     def car_brand(self):
#         return self.__brand + "!"

#     @car_brand.setter
#     def car_brand(self, brand):
#         self.__brand = brand
        
#     def full_name(self):
#         return f"{self.__brand}, {self.model}"
        
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod    # A static method is a method that belongs to a class rather than an instance of a class.
#     def general_description():     
#         return "Cars are means of trasnport!"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#       return "Electric charge"
      


# safari = Car("Tata", "Safari")

# print(Car.general_description())








## Property Decorators
## => Use a property decorator in the Car class to make the model attribute read-only

# class Car:
    
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     @property
#     def car_brand(self):
#         return self.__brand + "!"

#     @car_brand.setter
#     def car_brand(self, brand):
#         self.__brand = brand
        
#     def full_name(self):
#         return f"{self.__brand}, {self.__model}"
        
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod    # A static method is a method that belongs to a class rather than an instance of a class.
#     def general_description():     
#         return "Cars are means of trasnport!"
    
#     @property
#     def model(self):
#         return self.__model
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#       return "Electric charge"
      


# safari = Car("Tata", "Safari")
# # safari.model = "Nexon"
# print(safari.model)

# print(safari.__dict__)









## Class Inheritance and isinstance() function
## => Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.brand}, {self.model}"
    
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
    
# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
      






## Multiple Inheritance
## => Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand}, {self.model}"
 
class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
