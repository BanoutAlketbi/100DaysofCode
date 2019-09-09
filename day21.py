#--- length of a set
thisset = {'jojo', 'anna', 'helen', 'jenn'}
print(thisset)
print(len(thisset))

#--- to delete an item in a set we use remove() or discard()
thisset.remove('jenn')
thisset.discard('anna')
print(thisset)

thisset.discard('adam')

#--- pop() used to delete a random item in a set since it is not in order
y = {1, 34, 98, -2, 2}
x = y.pop()
print(x)
print(y)

#--- clear() is used to empty a set and del to delete the whole set
y.clear()
print(y)

# del y and i'll get an erorr

#--- set() constructor 
thisset1 = set(('hey', 'hello', 'hi'))
print(thisset1)
