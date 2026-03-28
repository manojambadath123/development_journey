

def find_pairs(arr, target):
    seen = set()
    pairs = []
    
    for num in arr:
        if target - num in seen:
            pairs.append((num, target - num))
        else:
            seen.add(num)
    
    return pairs

print(find_pairs([1,2,3,4,5], 5))  # [(3,2), (4,1)]