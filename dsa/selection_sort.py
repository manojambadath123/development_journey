# selection sort in ascending order
def selection_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        # min_index = i
        
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                # min_index = j
        
        # swap
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            #   arr[i], arr[j] = arr[j], arr[i]
    
    return arr


print(selection_sort([64, 25, 12, 22, 11]))


#selection sort in descending order

def selection_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        # min_index = i
        
        for j in range(i+1, n):
            if arr[i]<arr[j]:
                # min_index = j
        
        # swap
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            #   arr[i], arr[j] = arr[j], arr[i]
    
    return arr


print(selection_sort([64, 25, 12, 22, 11]))