def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

input_numbers = input("Enter the numbers: ")
numbers = list(map(int, input_numbers.split()))

sorted_numbers = bubble_sort(numbers)
print("Sorted A is:", sorted_numbers)
