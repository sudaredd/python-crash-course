from car import Car

class Battery():
    def __init__(self):
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has "+str(self.battery_size)+ " KWh battery")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
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
