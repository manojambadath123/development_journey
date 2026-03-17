

# lst = [10,11,11,12,13,13,14,15]


# lst.sort()

# for prev in range(0,len(lst)-1):

#     next = prev+1

#     diff = lst[next] - lst[prev]

#     if diff ==0:

#         print(lst[prev])


# lst = [10,11,11,12,13,13,14,15]

# st = set()
# lst.sort()

# for prev in range(0,len(lst)-1):

#     next = prev+1

#     diff = lst[next] - lst[prev]

#     if diff ==0:

#         st.add(lst[prev])

# print(st)



def find_duplicates(arr):


    for prev in range(0,len(arr)-1):

        next = prev+1

        diff = arr[next] - arr[prev]

        if diff ==0:

           print(lst[prev])



lst = [11,12,11,13,14,14]


lst.sort()

find_duplicates(lst)