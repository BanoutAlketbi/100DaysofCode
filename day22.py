#--- dictionary - dictionary name = { keys: value}
thisdict = {
    'brand': 'iMac',
    'version': 'macOS Sierra',
    'year': 2012
}
print(thisdict)
#--- accesing items is done by referring to its key name inside [] + get()
x = thisdict['year']
print(x)
y = thisdict.get('year')
print(y)

#--- changing the value is done by referring to its key name
thisdict['year'] = 2013
print(thisdict)

#--- looping through a dictionary
for z in thisdict: #--- for keys
    print(z)
for z in thisdict:
    print(thisdict[z]) #--- for printing values
for z in thisdict.values(): #--- used to also print values
    print(z)
#--- we can also use values without for loop
thisdict = {'name': 'Adam', 'age': 23, 'nnationality': 'Emratie'}
print(thisdict.values())

#--- items()is used to return all values and keys in a dictaionry
for a, b in thisdict.items(): #--- with for loop
    print(a, b)
#--- withour for loop
print(thisdict.items())
