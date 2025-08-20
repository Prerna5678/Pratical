def power(x, y):
    result = 1
    for i in range(x, y + 1):
        result *= x
    return result
