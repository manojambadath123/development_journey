

# def count_char_frequency(s):
    
#     frequency = {}
#     for char in s:
        
#         frequency[char] = frequency.get(char, 0) + 1

#     return frequency

# input_string = "hello world"
# char_counts = count_char_frequency(input_string)
# print(char_counts)


input_string = "hello world"
    
frequency = {}

for char in input_string:

    if char in frequency:
        
    # frequency[char] = frequency.get(char, 0) + 1
        frequency[char]+=1
    else:
        frequency[char] =1

        
print(frequency)