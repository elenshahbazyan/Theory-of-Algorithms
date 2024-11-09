def naive_string_match(T, P):
    n = len(T) 
    m = len(P) 

    for i in range(n - m + 1):
        s = 0
        while s < m and T[i + s] == P[s]:
            s += 1
        
        if s == m:
            print(f"Pattern found at index {i}")
            return i

T = "ABABDABACDABABCABAB"
P = "ABABCABAB"
naive_string_match(T, P)
