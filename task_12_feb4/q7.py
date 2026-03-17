
string = input("enter a string=")

vowels="aeiou"

count=0

for char in string:

    if char in vowels:

        count+=1
print("count of vowels in the string=",count)
