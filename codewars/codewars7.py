def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def backwards_prime(start, stop):
    result = []
    for num in range(start, stop + 1):
        if is_prime(num):
            reversed_num = int(str(num)[::-1])
            if num != reversed_num and is_prime(reversed_num):
                result.append(num)
    return result