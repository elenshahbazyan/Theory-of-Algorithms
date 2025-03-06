def merge_sort(A):
    if len(A) <= 1:
        return A
    mijin = len(A) // 2
    return merge(merge_sort(A[:mijin]), merge_sort(A[mijin:]))

def merge(left, right):
    sorted_A = []
    while left and right:
        sorted_A.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return sorted_A + left + right

numbers = list(map(int, input("Enter the numbers: ").split()))
sorted_numbers = merge_sort(numbers)
print("Sorted A is:", sorted_numbers)
