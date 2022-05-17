def main(args):
    dimentions = (200, 50)
    for dimention in dimentions:
        print (dimention)
    # throws exceptiom
    # dimentions[0]=32
    print(dimentions)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))