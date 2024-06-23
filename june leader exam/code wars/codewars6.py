def parts_sums(ls):
    sums = []
    n = sum(ls)
    sums.append(n)
    for i in ls:
        n = n - i
        sums.append(n)
    return sums