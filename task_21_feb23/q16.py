
person = {'name': 'Alice', 'age': 25}

name = person.get('name') 
print(f"Name: {name}") 


gender = person.get('gender')
print(f"Gender: {gender}") 


city = person.get('city', 'Unknown')
print(f"City: {city}") 