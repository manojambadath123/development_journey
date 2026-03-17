

lst = [10,11,12,11,10,13,13]

num_count = {n:lst.count(n)  for n in lst}

print(num_count)


# word = "racecar"

# char_count = {ch:word.count(ch)  for ch in word}

# print(char_count)



word = "racecarfast"

non_recursive_char = [ch for ch in word if word.count(ch)==1]

print("non recursive char=",non_recursive_char)

recursive_char = {ch:word.count(ch)  for ch in word if word.count(ch)>=2}

print("recursive char=",recursive_char)


