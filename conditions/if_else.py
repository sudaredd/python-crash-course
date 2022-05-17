def main(args):
    nested_coditions(12)
    nested_coditions(3)
    nested_coditions(19)
    nested_coditions(59)
    nested_coditions(61)

def nested_coditions(age):
    if age < 4:
        price=0;
    elif age < 18:
        price=4;
    elif age < 60:
        price=10;
    else:
        price=5;
    print("ur admission cost is "+str(price)+".")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))