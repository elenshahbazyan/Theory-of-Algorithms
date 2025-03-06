def find_odd_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [1, 2, 3, 2, 1]
print(find_odd_number(arr))
