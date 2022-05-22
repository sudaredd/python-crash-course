favourite_languages = {
    'jen':['java','python'],
    'sarah':['c','ruby'],
    'sudar':['java','go'],
    'edwin':['ruby'],
    'bill':['python','haskel']
}
for name, languages in favourite_languages.items():
    print("\n"+name.title()+" favourite languages are:")
    for language in languages:
        print("\t"+language.title())
