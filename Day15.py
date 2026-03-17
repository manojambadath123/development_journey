
# str1="Emma-is-a-data-scientist"
# res=''
# for i in str1:
#     if i!='-':
#         res+=i
#     else:
#         print(res)
#         res=''
# print(res)

# str1="Emma-is-a-data-scientist"
# a=str1.split('-')
# print(a)
# for i in a:
#     print(i)

# a="1010111100001111000000"
# count=0
# max_count=0
# for i in a:
#     if i=='0':
#         count+=1
#     else:
#         if count>max_count:
#             max_count=count
#         count=0
# if count>max_count:
#    max_count=count
# print(max_count)

# a="i am happy"
# op=''
# b=a.split()
# print(b)

# for i in b:
#     op=i+' '+ op
# print(op)

# a="i am happy"
# op=''
# current_word=''
# for i in range(len(a)):
#     if a[i]==' ':
#         op=current_word+' '+op
#         current_word=''
#     else:
#         current_word+=a[i]
# op=current_word+' '+op
# print(op)
        
# a="i am happy"
# op=''
# current_word=''
# for i in range(len(a)):
#     if a[i]!=' ':
#         current_word+=a[i]
        
#     else:
#         op=current_word+' '+op
#         current_word=''
        
# op=current_word+' '+op
# print(op)
        
# str=input("enter a string")
# if len(str)>=3:
#     if str[-3: ]=="ing":
#         str+="ly"
#         print(str)
#     else:
#         str+="ing"
#         print(str)
# else:
#     print(str)