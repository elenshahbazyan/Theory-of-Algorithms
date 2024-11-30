def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high and key >= arr[low] and key <= arr[high]:
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == key:
            return pos
        
        elif arr[pos] > key:
            high = pos - 1
        
        else:
            low = pos + 1
    
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
key = int(input("Search for: "))

A = interpolation_search(arr, key)
print(A)







