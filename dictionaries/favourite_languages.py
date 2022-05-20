favourite_languages = {
    'jen':'java',
    'sarah':'c',
    'sudar':'java',
    'edwin':'ruby',
    'bill':'python',
}
def loop_key_vals(favourite_languages):
    for name, language in favourite_languages.items():
        print("name :"+name)
        print("favourite language:"+language + '\n');

def loop_keys(favourite_languages):
    friends = ['jen', 'sarah']
    for name in favourite_languages.keys():
        print(name.title())
        if(name in friends):
            print("Hi "+name.title() + ", I see your favourite language is "+favourite_languages[name].title()+"!")


def sorted_order(favourite_languages):
    print("Enter sorted_order")
    for name in sorted(favourite_languages.keys()):
        print(name.title())
    print("Exit sorted_order")

def loop_values(favourite_languages):
    for language in favourite_languages.values():
        print("language "+language)

def set_loop_values(favourite_languages):
    print("set_loop_values enter")
    for language in set(favourite_languages.values()):
        print("language "+language)
    print("set_loop_values exit")

loop_key_vals(favourite_languages)
loop_keys(favourite_languages)
sorted_order(favourite_languages)
loop_values(favourite_languages)
set_loop_values(favourite_languages)