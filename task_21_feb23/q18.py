
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_remove = ['b', 'd', 'z'] # 'z' doesn't exist, but won't cause an error

for k,v in my_dict.items():

    print(k,v)

    if k