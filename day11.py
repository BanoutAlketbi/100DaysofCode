a = 2
print(a > 1 or a < 5)
print(a > 1 and a > -1)

#--- Identity Operators 
x = ['Dubai', 'Abu Dhabi']
y = ['Dubai', 'Abu Dhabi']
r = x
print(x is not r)
print(x is not y)
print(x !=y)
print(x is r)
print(y is r)

#--- in and not in
print('Dubai' in x)
print('Abu Dhabi' in y)
print('Shj' not in x)
print('Dubai' not in x)
