from dbm import dumb


class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("\n"+self.restaurant_name.title())
    
    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name.title() + " is opened")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Venilla', 'Chocoalte', 'Strawberry']
    
    def print_flavours(self):
        print("the flovours for today are ")
        for flavour in self.flavours:
            print("--"+flavour)
    
sapthagiri = Restaurant("Sapthagiri", 'South indian')
chipotle = Restaurant("Chipotle", 'Mexican')
papa_john = Restaurant("Papa johns", 'American')
dunkin = IceCreamStand("Baskin RObbins", 'American')

sapthagiri.describe_restaurant()
sapthagiri.open_restaurant()

chipotle.describe_restaurant()
chipotle.open_restaurant()

papa_john.describe_restaurant()
papa_john.open_restaurant()

dunkin.describe_restaurant()
dunkin.open_restaurant()
dunkin.print_flavours()


