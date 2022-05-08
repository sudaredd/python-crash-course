def exersises():
    name = 'Eric'
    print("Hello " + name + ", would you like to learn some Python today?")
    print(name.lower())
    print(name.upper())
    print(name.title())

    second = "Albert Einstein once said,\"A person who never made a mistake never tried anything new.\""
    print (second)
def main(args):
    name = "ada lovelace"
    print(name.title())
    name = "Ada Lovelace"
    print(name.upper())
    print(name.lower())
    
    first_name = "Ada"
    last_name = "Lovelace"
    full_name = first_name + " "+ last_name;
    print(full_name)
    print("Hello," + full_name + "!")
    print("Languages:\n\tPython\n\tC\n\tJavaScript")

    favorite_language = " python "
    print( favorite_language.lstrip())
    print( favorite_language.rstrip())
    print( favorite_language.strip())

    message = "One of Python's strengths is its diverse community."
    print(message)

    exersises()

    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
