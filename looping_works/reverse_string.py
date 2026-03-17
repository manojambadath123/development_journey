
# word = "python"

# result=""

# for i in range(5,-1,-1):

#     result+=word[i]

# print(f"reversed string= {result}")

word = input("enter a string=")

result=""

print(len(word))

for i in range(len(word)-1,-1,-1):

    result+=word[i]

print(f"reversed string= {result}")

