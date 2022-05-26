filename = 'text_files/pl_digits.txt'

def read_file_by_object(filename):
    with open(filename) as file_object:
    #contents = file_object.read()
        for line in file_object:
            print(line.rstrip())
        print("file read is done")

def read_file_ln(filename):
    with open(filename) as file_object:
        for line in file_object.readlines():
            print(line.rstrip())

#read_file_by_object(filename)
read_file_ln(filename)
