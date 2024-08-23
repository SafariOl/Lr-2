def calculation(n):
    sum = 0
    for val in range(1, n + 1):
        sum += (val+1)/val
    return sum