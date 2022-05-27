def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry the file "+filename + " doesn't exist")
    else:
        words = contents.split()
        num_words = len(words)
        print("file name "+filename + " has about "+ str(num_words) + " words")

filenames = ['alice.txt', 'siddartha.txt', 'pl_digits.txt', 'little_women.txt','pi_million_digits.txt']
for filename in filenames:
    count_words("text_files/"+filename)