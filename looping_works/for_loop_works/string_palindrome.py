
word = input("enter a string=")

reverse=""

for i in range(len(word)-1,-1,-1):

    reverse+=word[i]

print("reveresed string=",reverse)

if reverse==word:

    print("palindrome")
else:

    print("not palindrome")