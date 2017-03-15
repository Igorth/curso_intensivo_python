from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\n')
my_car = ElectricCar('jeep', 'troller', 2017)
print(my_car.get_descriptive_name())
my_car.battery.get_range()
my_car.battery.update_battery()
my_car.battery.get_range()