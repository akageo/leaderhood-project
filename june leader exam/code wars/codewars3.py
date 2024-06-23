def capitalize(s):
    even = ''
    odd = ''
    for i,x in enumerate(s):
        if i%2 == 0:
            even+= x.upper()
            odd += x
        else:
            even+= x
            odd += x.upper()
    return [even, odd]