

# word = "the quick brown fox jumps over lazy dog"

# alphabets="abcdefghijklmnopqrstuvwxyz"

# is_pangram = True

# for ch in alphabets:

#     if ch not in word:  #if word.find(ch)==-1

#         is_pangram = False

#         break

# print(is_pangram)


word = "the quick brown fox jumps over lazy dog"

alphabets="abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for ch in alphabets:

    if ch in word:  

        is_pangram = True

    else:

        is_pangram = False
        break
    

print(is_pangram)

