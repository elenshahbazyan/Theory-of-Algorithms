def selection_sort(A):
    n = len(A)

    for i in range(n):
        min_index = find_min_index(A, i, n)
        A[i], A[min_index] = A[min_index], A[i] 

    return A

def find_min_index(A, start, end):
    min_index = start
    for j in range(start + 1, end):
        if A[j] < A[min_index]:
            min_index = j
    return min_index


input_numbers = input("Enter the numbers: ")
numbers = list(map(int, input_numbers.split()))

sorted_numbers = selection_sort(numbers)
print("Sorted numbers:", sorted_numbers)

