def main(args):
    print20()
    #list_print_million()
    list_stas_nillion()
    multiples_of_3()
    cubes_10()

def cubes_10():
    cube_list = []
    print("print first 10 cubes")
    for i in range(1,11):
        cube_list.append(i**3)
    for num in cube_list:
        print (num)
    cl = [i**3 for i in range(1,11)]
    print("print cubes with list function")
    for i in cl:
        print (i)

def multiples_of_3():
    list_3 = [ i*3 for i in  (range(1, 11)) ]
    print("multiples of 3")
    for num_ in list_3:
        print(num_)
    print("multiples of 3 with list function")
    list_33 = list(range(3, 31, 3))
    for num in list_33:
        print (num)


def list_stas_nillion():
    million_list = list(range(1, 1000001))
    print(min(million_list))
    print(max(million_list))
    print(sum(million_list))


def list_print_million():
    million_list = list(range(1, 1000001))
    for num in million_list:
        print(num)
    print("printed million records")

def print20():
    for num in range(1, 21):
        print(num)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))