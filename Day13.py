
a=" PyThon Is A prOGraMMing Language 1234!@##$"
uppercase=0
lowercase=0
digit=0
special=0

for i in a:
    if i.islower():
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
alpha=lowercase + uppercase
print(lowercase)
print(uppercase)
print(digit)
print(special)
print(alpha)

