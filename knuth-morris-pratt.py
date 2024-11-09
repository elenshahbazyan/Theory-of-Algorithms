def boyer_moore(T, P):
    def BadMatchTable(pattern):

        last = {}
        m = len(pattern)
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

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
            return f"Pattern found at index {i}"
        else:
            i += max(1, j - L.get(T[i + j], -1))
    
    return "Pattern not found"

text = "MY NAME IS ELEN"
pattern = "ELEN"

result = boyer_moore(text, pattern)
print(result)


