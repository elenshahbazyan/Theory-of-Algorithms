def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

n=int(input("Enter the number of elements:"))
A = []
for i in range(n):
    num = int(input(f"Enter number {i+1}:"))
    A.append(num)

insertion_sort(A)
print(A)
        
