import math

def jump_search(arr, search):
    n = len(arr)
    step = int(math.sqrt(n))
    jump_from = 0
    while arr[min(step, n) - 1] < search:
        jump_from = step
        step += int(math.sqrt(n))
        if jump_from >= n:
            return -1
    for i in range(jump_from, min(step, n)):
        if arr[i] == search:
            return i
    return -1

arr = list(map(int, input("Enter the elements: ").split()))
search = int(input("Search for: "))

A = jump_search(arr, search)
print(" Found at index" , A)





