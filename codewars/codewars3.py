def repeats(arr):
    sum = 0
    for x1 in arr:
        status = 0
        for x2 in arr:
            if x1 == x2:
                status += 1
        if status == 1:
            sum += x1
    return sum