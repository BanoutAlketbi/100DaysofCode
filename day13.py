#--- list for num
numbers = [10, 20, 30, 40]
print(numbers)

#--- list for strings
thislist = ['Dubai', 'Abu dhabi', 'Ajman']
print(thislist)

#--- list for both num and strings
numstr = ['Dubai', 'Abu Dhabi', 20, 40]
print(numstr)

#--- list for decimal
dec = [1.0, 2.0, -2.3]
print(dec)

#--- using index to get an item 
print(thislist[2])
print(thislist[0])

#--- for loop
for x in thislist:
    print(x)

q = [ 1, 56, 71, -3, 2, 100]
for x in q:
    print(x)

#--- changing an item in a list
thislist[2] = 'Sharjah'
print(thislist)

numstr[2] = 21
print(numstr)

#--- to delete we use del
cities = ['LA', 'Munich', 'Newyork', 'Delhi']
del cities[3]
print(cities)

y = [1, 2, 4, -4]
del y
print(y)