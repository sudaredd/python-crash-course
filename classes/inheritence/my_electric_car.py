from car import ElectricCar
my_tesla = ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.read_odometer())
print(my_tesla.battery.get_range())