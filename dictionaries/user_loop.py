user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

# for key, val in user_0.items():
#     print("key "+key + " and value "+val)

for val in user_0.values():
    print ("value is ", val)

# Initialize an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary only if key doesn't exist
my_dict.setdefault('key1', set())
my_dict.setdefault('key2', [])

# Append elements to the list corresponding to the keys
my_dict['key1'].add('value1')
my_dict['key1'].add('value1')
my_dict['key1'].add('value2')
my_dict.setdefault('key1', set()).add('valuenkk')


my_dict['key2'].append('value3')
my_dict['key2'].append('value4')

# Add element to a non-existing key
my_dict.setdefault('key3', []).append('value5')

# Print the dictionary
print(my_dict)
