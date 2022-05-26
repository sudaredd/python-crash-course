filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pl_string = ""
for line in lines:
    pl_string += line.rstrip()
print(pl_string)
birth_day = input('Ente ur birth day ')
if birth_day in pl_string:
    print("ur birthday appears in millions of pl")
else :
    print("ur birthday doesn't appear in millions of pl")