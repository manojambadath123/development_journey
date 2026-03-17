
word1 = input("enter word1=")
word2 = input("enter word2=")

if len(word1) > len(word2):

    print(word1[len(word2):])

elif len(word2) > len(word1):

    print(word2[len(word1):])

else:

    print("no balance string")












