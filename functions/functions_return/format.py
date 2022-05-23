def format_name(first_name, last_name, middle_name=''):
    if(middle_name):
        full_name = first_name + ' '+ middle_name + ' '+last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

def build_person(first_name, last_name, middle_name=''):
    dict = {
        'firstName':first_name, 'lastName':last_name
    };
    if(middle_name):
        dict['middleName'] = middle_name

    return dict


s_name = format_name('sudar', 'kasir', 'reddy')
p_name = format_name('pras', 'kasir')
b_name = format_name('bvya', 'kasir')
d_name = format_name('dvya', 'kasir')
print(s_name)
print(p_name)
print(b_name)
print(d_name)
person = build_person('sudar', 'kasir', 'reddy')
print(person)