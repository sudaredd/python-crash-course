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