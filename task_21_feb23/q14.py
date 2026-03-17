
keys_list = ['name', 'age', 'city']

values_list = ['Alice', 30, 'New York']

my_dict = {}

for key, value in zip(keys_list, values_list):
    
    my_dict[key] = value

print(my_dict)