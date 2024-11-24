def hanoi(n , start, end, other):
    if n==1:
        print ("Move disk 1 from start",start,"to end",end)
        return
    hanoi(n-1, start, other, end)
    print ("Move disk",n,"from start",start,"to end",end)
    hanoi(n-1, other, end, start)
        
n = int(input("Enter the number:"))
hanoi(n,'A','B','C') 
