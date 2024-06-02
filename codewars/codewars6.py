def dig_pow(n, p):
    r = 0
    for i in str(n):
        r += int(i)**p
        p += 1
    
    k = r / n
    if k == int(k):
        return k
    return -1