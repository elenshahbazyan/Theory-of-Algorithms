import heapq

def heapsort(A):
    heapq.heapify(A)
    n = len(A)
    new_list = [0] * n

    for i in range(n):
        minimum =heapq.heappop(A)
        new_list[i] = minimum

    return new_list

sorted_list = heapsort([1,3,5,7,9,2,4,6,8,0])
print(sorted_list)

