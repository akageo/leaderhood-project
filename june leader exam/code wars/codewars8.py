def solution(array_a, array_b):
    c = 0
    output = 0
    while c < len(array_a):
        
        temp = abs(array_a[c] -array_b[c])
        
        output += temp **2
        
        c +=1
    
    
    return output / len(array_a)