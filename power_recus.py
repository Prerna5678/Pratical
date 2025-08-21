def power(x, y):
    result = 1
    for i in range( y+1):
        print(i)
        result *= x
    return result
print(power(2,5))