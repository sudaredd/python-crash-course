def main(args):
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print (bicycles)
    print (bicycles[0])
    print (bicycles[0].title())
    print (bicycles[3])
    print (bicycles[-1])
    modify()
    add_insert()
    remove()
    sort()
    reverse()
    loop()

def loop():
    print("==========================loop starts==========================")
    
    magicians = ['alice', 'david', 'carolina']
    
    for magician in magicians:
        print (magician.title() + ", that was a great trick");
        print("I can't wait for your next trick, "+magician.title() + ".\n")
    
    print("==========================loop ends==========================")
def reverse(): 
    print('-------------Reverse starts---------------------------')
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(cars)
    cars.reverse()
    print(cars)
    print('-------------Reverse ends---------------------------')

def sort():
    print('-------------Sort starts---------------------------')
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()
    print(cars)
    cars.sort(reverse=True)
    print("reverse sort=>"+str(cars))
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(sorted(cars, reverse=True))
    print('-------------Sort ends---------------------------')

def modify():
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles[-1] = 'ducati';
    print(motorcycles)

def add_insert():
    cars = []
    cars.append("Honda")
    print (cars)
    cars.append("Ford")
    cars.append("GM")
    print ("after added 3 "+ str(cars))
    cars.insert(0, "Toyota")
    print ("after inserted "+ str(cars))

def remove():
    cars = ['Honda', 'Nissan', 'Toyoya', 'Ford']
    print (cars)
    del cars[2]
    print (cars)
    print("poped last element "+cars.pop());
    print ("after pop "+str(cars))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))