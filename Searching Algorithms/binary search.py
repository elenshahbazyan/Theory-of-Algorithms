def binary_search(arr, search):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
search = int(input("Search for: "))

A = binary_search(arr, search)

print("Found at index:" ,A)


