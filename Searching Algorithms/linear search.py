def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
search = int(input("Search for: "))

A = linear_search(arr, search)

print("Found at index:", A)




