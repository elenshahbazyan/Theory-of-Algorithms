def ternary_search(arr, search):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == search:
            return f"Element {search} found at index {mid1}"
        elif arr[mid2] == search:
            return f"Element {search} found at index {mid2}"
        if search < arr[mid1]:
            right = mid1 - 1
        elif search > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return f"Element {search} not found in the list"

arr = list(map(int, input("Enter the elements: ").split()))
search = int(input("search for: "))

A = ternary_search(arr, search)

print(" Found at index:",A)



