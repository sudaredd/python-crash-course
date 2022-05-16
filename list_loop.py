def main(args):
   # forloop()
    for_range()
    range_list()
    range_squares_list()
    stats_list_numbers()

def stats_list_numbers():
    digits = list(range(0, 11))
    print (digits)
    print (min(digits))
    print (max(digits))
    print (sum(digits))

def range_squares_list():
    squares = []
    for num in range(1, 11):
        square = num**2
        squares.append(square)
    print (squares)


def range_list():
    numbers = list(range(1,6))
    numbers.append(7)
    print(numbers)
    even_numbers = list(range(0, 11, 2))
    odd_numbers = list(range(1, 11, 2))
    print(even_numbers)
    print(odd_numbers)

def for_range():
    for value in range(1,6):
        print("value=>"+str(value))

def forloop():
    magicians = ['alice','david','carolina']
    for magician in magicians:
        print(magician.title() + ', that was a great trick!')
        print("I can't wait to see ur next trick "+ magician.title() + ".\n")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))