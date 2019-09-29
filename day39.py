def pwr_recursion (num, pwr):
    if pwr > 0:
        result = num * pwr_recursion(num, pwr-1)
    else:
        result = 1
    return result
print(pwr_recursion(5,3))
