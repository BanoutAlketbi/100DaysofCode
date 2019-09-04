#--- Tuple
thistuple = ("Dubai", "Abu Dhabi", "Al Ain")
print(thistuple)
thistuple = ()
print(thistuple)
thistuple = (12,) #--- if a tuple has one item we must put a comma after the item
print(thistuple)
thistuple = (1, 23.5, -34,1)
print(thistuple)
thistuple = ('Mariam', -22, 0.1, "بايثون") #--- tuple can hold more than one data type
print(thistuple)

#---to get to a tuple item we use index numbers, e.g [1] means that you want to access item num1 in that tuple
thistuple = ("Dubai", "Abu Dhabi", "Al Ain")
print(thistuple[2])
print(thistuple[0])

#--- for loop to loop through a tuple's items
thistuple = ("Dubai", "Abu Dhabi", "Al Ain")
for x in thistuple:
    print(x)
#--- to print the wanted items of a tuple we use index
f = (23, 45, 56,2,-3, 56)
print(f[2:4])

#--- we can't change items
x = ('F1', 'F2', "F4")    
x [1] = "F7" #-- it wont work as we can change the value of items in a tuple
print(x)

#--- we can only delete the whole tuple using del, in tuples we can't delete one item only the whole tuples
del thistuple
print(thistuple)