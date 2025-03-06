def boyer_moore(T, P):
    def BadMatchTable(pattern):

        dictionary = {}
        m = len(pattern) 
        for i in range(len(pattern)):
            dictionary[pattern[i]] = m - 1 - i 
        return dictionary

    L = BadMatchTable(P)
    m = len(P)  
    n = len(T)  
    i = 0  

    print(L)

    while i <= n - m:
        j = m - 1  
        while j >= 0 and T[i + j] == P[j]:
            j -= 1  

        if j == -1:
            return i

        else:
    
            shift = L.get(T[i + j], m)  
            i += shift  

    return -1

text = "MY NAME IS ELEN"
pattern = "ELEN"

B = boyer_moore(text, pattern)
print(B)
