# dictionary = A changeable, unordered collection of unique key:value pairs
#              fast because they are hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'Russia':'Moscow'}

# print(capitals.get('USA'))
# print(capitals.keys())
print(capitals.items())
for keys,values in capitals.items():
    print(keys,end=",")
