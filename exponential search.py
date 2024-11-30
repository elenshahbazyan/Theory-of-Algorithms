def exponential_search(arr, search):
    if arr[0] == search:
        return 0
    
    n = len(arr)
    i = 1
    while i < n and arr[i] <= search:
        i *= 2
    
    low = i // 2
    high = min(i, n - 1)
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
search = int(input("search for: "))

A = exponential_search(arr, search)
print(A)










