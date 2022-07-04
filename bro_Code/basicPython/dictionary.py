#Dictionary = a changeable, unordered collection of unique key: value pairs.
#It is fast because they use hashing and allow us to access a value quickly

from multiprocessing.sharedctypes import Value


capitals = {'Abia': 'Umuahia',
            'Imo': 'Owerri', 
            'Rivers': 'Bayelsa',
            'Enugu': 'Awka'
            }

#print(capitals['Rivers']) #this gives an error if 
                           # #the state's name is not on your dictionary.

print(capitals.get('Anambra'))  # This will print NONE if the name is not on your dictionary.

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({'Anambra':'Awka'})

print(capitals.items())