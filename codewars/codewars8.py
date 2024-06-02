def rot13(message):
    res = ''
    for i in message:
        if i.isalpha():
            if (ord(i) > 64 and ord(i) < 78) or (ord(i) > 96 and ord(i) < 110):
                res = res+chr(ord(i)+13)
            else:
                res = res + chr(ord(i) - 13)
        else:
                res += i
        
    return res
                                                 
