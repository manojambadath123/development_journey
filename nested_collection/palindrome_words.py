

# words = ["mad","test","tan","dad","stats","racecar"]

# palindrome_words = [w  for w in words  if w[::-1]==w]

# print(palindrome_words)


word = "malayalam"
rev = ""
for i in range(len(word)-1,-1,-1):

    rev+= word[i]

if (rev == word):

    print("palindrome")

else:

    print("not palindrome")

# words = ["mad","test","tan","dad","stats","racecar"]

# palindrome_words = [w  for w in words  if w[::-1]==w]

# print(palindrome_words)
