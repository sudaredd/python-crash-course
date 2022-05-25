from car import Car
from my_electric_car import ElectricCar

nissan = Car('Nissan', 'Sentra', 2005)
print(nissan.get_descriptive_name())
nissan.read_odometer()

my_tesla = ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
print(my_tesla.battery.get_range())