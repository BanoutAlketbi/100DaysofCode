num = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
print(num)
for y in num:
    x = lambda a: print(a) if a > 0 else None
    x(y)