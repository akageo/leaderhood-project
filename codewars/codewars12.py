def permutations(s):
    if len(s) == 1:
        return [s]
    
    all_permutations = []
    
    for i in range(len(s)):
        current_char = s[i]
        
        rest = s[:i] + s[i+1:]
        
        for p in permutations(rest):
            all_permutations.append(current_char + p)
    
    unique_permutations = list(set(all_permutations))
    
    return unique_permutations