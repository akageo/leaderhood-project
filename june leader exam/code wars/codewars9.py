def valid_ISBN10(isbn): 
    if len(isbn)!=10:
        return False
    s=0
    a='1234567890'
    for i in range(0,10):
        if isbn[i]=='X':
            if i==9:
                s+=(i+1)*10
            else:
                return False
        else:
            if isbn[i] in a:
                s+=(i+1)*int(isbn[i])
            else:
                return False
    if s%11==0:
        return True
    else:
        return False