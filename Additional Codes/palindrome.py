def palindrome(T):
    n = len(T)
    for i in range(n // 2):
        if T[i] != T[n - i - 1]:
            return False
    return True

def find_longest_palindrome(S):
    m = len(S)
    max_length = 0
    start_index = 0
    
    for k in range(m, 0, -1): 
        for i in range(m - k + 1): 
            substring = S[i:i + k]
            if palindrome(substring):
                if k > max_length:
                    max_length = k
                    start_index = i
    return start_index, max_length

def can_be_palindromic(S):
    char_count = {}
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


S = "abghjkadsasdaadsakjhgcxlilktdf"

start, length = find_longest_palindrome(S)
print("Palindrome starts at index:", start)
print("Largest palindrome length is:", length)
print("Longest palindromic substring is:", S[start:start + length])

if can_be_palindromic(S):
    print("The string can be rearranged into a palindrome.")
else:
    print("The string cannot be rearranged into a palindrome.")

