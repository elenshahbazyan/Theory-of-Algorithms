def failureFunction(P):
    m = len(P)
    F = [0] * m 
    length = 0  
    i = 1  

    while i < m:
        if P[i] == P[length]:
            length += 1
            F[i] = length
            i += 1
        else:
            if length != 0:
                length = F[length - 1]  
            else:
                F[i] = 0
                i += 1

    return F


def KMPMatch(T, P):
    n = len(T)
    m = len(P)

    F = failureFunction(P)

    t = []
    i = 0
    j = 0

    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1

        if j == m:
            t.append(i - j)  
            j = F[j - 1]  

        elif i < n and P[j] != T[i]:
            if j != 0:
                j = F[j - 1]  
            else:
                i += 1

    return t



T = "ababdabacdababcabab" 
P = "ababcabab"

t = KMPMatch(T, P)
print(failureFunction(P))
print(t)


