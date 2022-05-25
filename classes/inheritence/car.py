class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Fills the gas tank!")

class Battery():
    def __init__(self):
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has "+str(self.battery_size)+ " KWh battery")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240;
        elif self.battery_size == 85:
            range = 275
        message = "This car go approximately "+ str(range)
        message += " with full charge"
        return message

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
print(my_tesla.battery.get_range())
my_tesla.fill_gas_tank()