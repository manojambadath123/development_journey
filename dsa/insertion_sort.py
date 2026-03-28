
# insertion sort in ascending order

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr


# Example
print(insertion_sort([12, 11, 13, 5, 6]))

# insertion sort in descending order

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr


# Example
print(insertion_sort([12, 11, 13, 5, 6]))
