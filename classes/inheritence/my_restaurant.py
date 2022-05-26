from restaurant import Restaurant, IceCreamStand

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