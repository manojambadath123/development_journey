
def num_vowels(string):

    vowels="aeiou"
    count=0

    for char in string:

        if char in vowels:

            count+=1

    return count


result = num_vowels("python")

print(f"count of vowels in the string is {result}")



