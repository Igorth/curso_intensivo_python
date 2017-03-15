from car import Car
from electric_car import ElectricCar 
#import car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())