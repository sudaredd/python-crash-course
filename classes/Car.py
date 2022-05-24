class Car():
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' '+self.model
        return long_name
    
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading) + ' miles on it\n')
    
    def update_odometer(self, milage):
        if(milage > self.odometer_reading):
            self.odometer_reading = milage
        else:
            print("You can't rollback odometer, update odometer milage is less than current odometer reading "+str(self.odometer_reading))

    def increment_odometer(self, miles):
        self.odometer_reading +=miles

nissan = Car('Nissan', 'Sendtra', 2005)
crv = Car('Honda', 'CRV', 2007)

print(nissan.get_descriptive_name())
nissan.read_odometer()

print(crv.get_descriptive_name())
crv.read_odometer()

crv.odometer_reading = 86000
crv.read_odometer()

nissan.update_odometer(120000)
nissan.read_odometer()
nissan.update_odometer(9000)
nissan.increment_odometer(11500)
nissan.read_odometer()
