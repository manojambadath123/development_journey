
# a="hello good morning hi"
# b=a.split()
# print(b)
# for i in b:
#     if len(i)%2==0:
#         print(i,end=' ')


# a="hello good morning hi"
# word=''
# for i in a:
#     if i!=' ':
#         word+=i
#     else:
#         if len(word)%2==0:
#             print(word,end=' ')
#         word=''
# if len(word)%2==0:
#     print(word,end=' ')

# str="pYThoN"
# lower="abcdefghijklmnopqrstuvwxyz"
# upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ind=0
# op=''
# for i in str:
#     if i in lower:
#         ind=str.index(i)
#         op+=str[ind].upper()
#     else:
#         ind=str.index(i)
#         op+=str[ind].lower()
# print(op)

# str="pYThoN"
# op=''

# for i in str:
#     if i.isupper():
#         op+=i.lower()
#     else:
#         op+=i.upper()
# print(op)

# a="hello good evening"
# b=a.title()
# print(b)

# a="hello good evening"
# word=''
# op=''
# for i in a:
#     if i!=' ':
#         word+=i
#     else:
#         if word!='':
#            op+=word[0].upper()+word[1: ].lower()+' '
#            word=''
# if word!='':
#    op+=word[0].upper()+word[1: ].lower()+' '
# print(op)

# a="hello good evening"
# word=''
# op=''
# for i in a:
#     if i!=' ':
#         word+=i
#     else:
        
#            op+=word[0].upper()+word[1: ].lower()+' '
#            word=''

# op+=word[0].upper()+word[1: ].lower()+' '
# print(op)

# a="hello good evening"
# vowel="aeiou"
# count_v=0
# count_c=0

# for i in a:
#     if i in vowel:
#         count_v+=1
#     else:
#         count_c+=1
# print(count_v)
# print(count_c)

# a="hello good eveningEE"
# vowel="aeiouAEIOU"
# count_v=0
# count_c=0

# for i in a:
#     if i in vowel:
#         count_v+=1
#     else:
#         count_c+=1
# print(count_v)
# print(count_c)

# a=365
# largest_digit=0

# while(a>0):
#     temp=a%10
#     if temp>largest_digit:
#         largest_digit=temp
#     a//=10

# print(largest_digit)
