

# arr = [2,3,4,5]

# arr.sort()

# sum = 8


# for prev in range(0,len(arr)-1):

#     next = prev + 1

#     if arr[prev] + arr[next] ==sum:

#         print(arr[prev],arr[next])



arr = [2,3,4,5]

arr.sort()

sum = 8

left=0
right=len(arr)-1

while(left<right):

     current_sum = arr[left] + arr[right]

     if current_sum==sum:
          
          print(arr[left],arr[right])

          left+=1
          right-=1

     elif current_sum > sum:
          
          right-=1

     elif current_sum < sum:
          
          left+=1
          


  










