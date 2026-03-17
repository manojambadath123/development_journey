

"""

w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6



"""


# list = [1,2,3,5]

# print(list)

# length = len(list)

# for i in range(1,length+1):

#     if i not in list:

#         print(i,"is missing")

#         break

# else:

#     print(length+1,"is missing")


# list = [1,2,3,5]

# list.sort()

# print(list)

# prev = 0

# next = prev+1

# for i in range(1,len(list)-1): 

#     diff = list[i+1] - list[i]

#     if diff!=1:

#         print(list[i]+1,"is missing")



# list = [1,2,3,5]

# list.sort()

# print(list)

# prev = 0

# next = prev+1

# while(prev<=len(list)-2):

#     diff = list[next] - list[prev]

#     if diff!=1:

#         print(list[prev]+1,"is missing")

#         break


#     prev+=1
#     next = prev+1



# def missing_least_positive(arr):

#    prev = 0

#    next = prev+1

#    while(prev<=len(arr)-2):

#        diff = arr[next] - arr[prev]

#        if diff!=1:

#             print(arr[prev]+1,"is missing")

#             break


#        prev+=1
#        next = prev+1




# list = [1,2,3,5]

# list.sort()

# print(list)

# missing_least_positive(list)




def missing_least_positive(arr):

   

   for prev in range(0,len(arr)-1):
       
       

       next = prev+1

       diff = arr[next] - arr[prev]

       if diff!=1:

            print(arr[prev]+1,"is missing")

            break


   else:
       
       print(arr[prev]+1,"is missing")
         
       





list = [1,2,3,5]

list.sort()

print(list)

missing_least_positive(list)

