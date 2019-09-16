#---if
a = 12
b = 100
if b > a:
    print('b is greater than a')
if a > b:
    print('b is greater than a')
#---elif
a = 1
b = 1
if b < a:
    print('b is less than a')
elif a == b:
    print('b is equal to a')
#---else
a = 100
b = 1
if b > a:
    print('b is greater than a')
elif a == b:
    print('b is equal to a')
else:
    print("a is greater than b")
#--- using else withut elif
a = 23
b = 90
if b < a:
    print('b is less than a')
else:
    print('b is greater than a')
#---short hand if
a = 150
b = 120
if a != b: print('a and b are not equals')
#---short if else
a = 20
b = 120
print("A") if a > b else print('B')
a = 5
b = 5
print("A") if a > b else print('=') if a == b else print('B')
#---and
a = 100
b = 120
c = 190
if c > a and c > b:
    print('c is greater than both a and b')
#--or and nested if
a = 100
b = 300
c = 250
if a < b or c > a: print('one of the conditions is true')
x = 20
if x > 10 :
    print('x is above 10,')
    if x > 15:
        print('and 15,')
    else:
        print('but not above 30')
