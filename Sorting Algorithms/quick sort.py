def quick_sort(A):
    if len(A) <= 1:
        return A
    B = A[len(A) // 2]
    left = [x for x in A if x < B]
    middle = [x for x in A if x == B]
    right = [x for x in A if x > B]
    return quick_sort(left) + middle + quick_sort(right)

numbers = list(map(int, input("Enter the numbers: ").split()))
sorted_numbers = quick_sort(numbers)
print("Sorted A is:", sorted_numbers)
