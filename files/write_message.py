filename = 'programming.txt'

def write_file(filename):
    with open(filename, 'w') as file_object:
        file_object.write("I love programming\n")
        file_object.write("I love creating games\n")
    print('file writer is done')

def append_file(filename):
    with open(filename, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")
    print('file append is done')

write_file(filename)
append_file(filename)