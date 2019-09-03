#--- len() is used to know the# of items in a list
a = ['a', 'b', 'c', 'e']
print(len(a))

#--- to add a new item in a list we use append()
a.append('s')
print(a)
print(len(a))

#--- to insert a new item into an index
a.insert(2, 'p')
print(a)

#--- to remove an item we use either remove() or pop()
a.remove('a')
print(a)
b = ['Mariam', 'Mariam', 'Moahmed']
b.remove('Mariam')
print(b)

b.pop()
print(b)
b.pop(0)
print(b)

#--- clear() is used to clear the whole list
b.clear()
print(b)

#--- to copy a list we use copy() or list()
thislist= ['Pizza', 'Pasta', 'Salad']
mylist = thislist.copy()
print(mylist)
thislist.remove('Pasta')
print(thislist)
print(mylist)

yourlist = list(thislist)
print(yourlist)

#--- to make a new list we use list() \\ WE USE () not []
f = list(('x', 'y', 'F1', 'F5'))
print(f)

#-------
f.extend('b')
print(f)
f.reverse()
print(f)