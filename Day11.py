
# s=input("enter a string")
# rev=""
# index=len(s)-1
# while index>=0:
#     rev+=s[index]
#     index-=1

# print(rev)

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(i):
#       print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(i):
#       print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(1,row+1):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(' ',end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for  i in range(row,0,-1):
#     for j in range(row-i):
#         print(' ',end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     for k in range(row-i):
#         print(' ',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(row-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(row-i)-1):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(row-i)-1):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(row-i-1):
#         print(' ',end=' ')
#     for k in range(2*i+1):
#         print('*',end=' ')
#     print()

# row=int(input("enter rows"))
# for i in range(row):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(2*(row-i)-1):
#         print('*',end=' ')
#     print()


# row=int(input("enter a row"))
# for i in range(row):
#     for k in range(2*i+1):
#         print('*',end=' ')
#     # for j in range(i):
#     #     print(' ',end=' ')
#     print()

# rows=int(input("enter rows"))
# for i in range(1,rows+1):
#     for k in range(i):
#         print('*',end=' ')
#     for j in range(rows-1):
#         print(' ',end=' ')

#     print()

# for l in range(rows-1,0,-1):
#     for m in range(l):
#         print('*',end=' ')
#     for n in range(rows-l):
#         print(' ',end=' ')
#     print()

# rows=int(input("enter rows"))
# for i in range(1,rows+1):
#     for k in range(rows-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')

#     print()

# for l in range(rows-1,0,-1):
#     for m in range(rows-l):
#         print(' ',end=' ')
#     for n in range(l):
#         print('*',end=' ')
#     print()

rows=int(input("enter rows"))
for i in range(rows):
    for j in range(rows-i-1):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()

for l in range(rows-1,0,-1):
    for m in range(rows-l):
        print(' ',end=' ')
    for n in range(2*l-1):
        print('*',end=' ')
    print()
