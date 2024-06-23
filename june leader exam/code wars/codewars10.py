def lcm(*args):
    if len(args) == 0:
        return 1
    
    for i in args:
        if i == 0:
            return 0
    args = sorted(args)
    max1 = max(args)
    max2 = max(args)
    j = 2
    a = True
    while a:
        for i in args:
            if max2 % i != 0:
                a = True
                max2 = max1 * j
                j += 1
                break
            else: 
                a = False

    return max2