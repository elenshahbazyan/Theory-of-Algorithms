NO_OF_CHARS = 256

def getNextState(pattern, pattern_length, current_state, char): 
    if current_state < pattern_length and char == ord(pattern[current_state]): 
        return current_state + 1
    
    for state in range(current_state, 0, -1): 
        if ord(pattern[state - 1]) == char: 
            match = True
            for i in range(state - 1): 
                if pattern[i] != pattern[current_state - state + 1 + i]: 
                    match = False
                    break
            if match:  
                return state 
    return 0  

def buildTransitionTable(pattern, pattern_length): 
    transition_table = [[0] * NO_OF_CHARS for _ in range(pattern_length + 1)] 

    for state in range(pattern_length + 1): 
        for char in range(NO_OF_CHARS): 
            transition_table[state][char] = getNextState(pattern, pattern_length, state, char) 

    return transition_table 

def searchPattern(pattern, text): 
    pattern_length = len(pattern) 
    text_length = len(text) 

    transition_table = buildTransitionTable(pattern, pattern_length) 

    current_state = 0
    for i in range(text_length): 
        current_state = transition_table[current_state][ord(text[i])] 
        if current_state == pattern_length:  
            print(f"Pattern found at index: {i - pattern_length + 1}")

def main(): 
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    searchPattern(pattern, text) 

if __name__ == '__main__': 
    main()


