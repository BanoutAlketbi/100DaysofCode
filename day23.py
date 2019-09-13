#--- to check if a key exits we use in 
thisdict = {
    'brand': 'iMac',
    'version': 'macOS Sierra',
    'year': 2012
}
if 'brand' in thisdict:
    print('Yes, brand is one of the keys')
#--- we use len() to determine how many items in a dictionary
print(len(thisdict))

#--- to add a new item we use a new index key
thisdict['color'] = 'white'
print(thisdict)

#--- to remove an item we use either pop() or poptime() - last added item, del() and clear()
x = {
    'F1': 'A',
    'F2': 23,
    'F4': 'B'
}
print(x)
x.pop('F1')
print(x)

x.popitem()
print(x)
del x #--- will delete it and show an error when printing NameError: name 'x' is not defined


thisdict.clear()
print(thisdict)
