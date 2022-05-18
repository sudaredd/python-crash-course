def print_stages(age):
    if age < 2:
        person = 'a baby'
    elif age >= 2 and age < 4:
        person = 'a toddler'
    elif age >= 4 and age < 13:
        person = 'a kid'
    elif age >=13 and age < 20:
        person = 'a teenager'
    elif age >=20 and age < 65:
        person = 'an adult'
    else:
        person = 'an elder'
    print ("the person is "+person)
print_stages(1)
print_stages(2)
print_stages(5)
print_stages(19)
print_stages(59)
print_stages(65)
