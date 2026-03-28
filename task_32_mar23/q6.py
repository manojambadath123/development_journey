


word = input("enter a word=")

rev=""

for i in range(len(word)-1,-1,-1):

    rev+= word[i]


if (rev==word):

    print("palindrome")

else:

    print("not palindrome")

