strings = ["abab" , "aba" , "abbda", "ab"]











































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                return A
A = ["abab" ,"aba" ,"abbda" , "ab"]
sorted_A = bubble_sort(A)
sorted_A
                







































sorted_strings = sorted(strings)

print(sorted_strings)
