class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("\n"+self.restaurant_name.title())
    
    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name.title() + " is opened")
    
sapthagiri = Restaurant("Sapthagiri", 'South indian')
chipotle = Restaurant("Chipotle", 'Mexican')
papa_john = Restaurant("Papa johns", 'American')

sapthagiri.describe_restaurant()
sapthagiri.open_restaurant()

chipotle.describe_restaurant()
chipotle.open_restaurant()

papa_john.describe_restaurant()
papa_john.open_restaurant()


