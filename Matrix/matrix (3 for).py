n = int(input("Enter the number of rows for matrix A and columns for matrix B: "))
m = int(input("Enter the number of columns for matrix A / rows for matrix B: "))


print("Enter the elements of matrix A:")
A = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)


print("Enter the elements of matrix B:")
B = []
for i in range(m):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)


C = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        C[i][j] = 0
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]


print("\nMatrix C (Result of A x B):")
for row in C:
    print(row)
