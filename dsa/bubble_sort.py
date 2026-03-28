
# bubble sort in ascending order
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                
                # arr[j]  = arr[j+1] 
                # arr[j+1] = arr[j]
    
    return arr



print(bubble_sort([5, 3, 1, 4]))

#bubble sort in descending order

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        for j in range(0, n-i-1):

            if arr[j] < arr[j+1]:

               temp = arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=temp
            
            # if arr[j] < arr[j+1]:
            #     # swap
            #     arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr



print(bubble_sort([5, 3, 1, 4]))


