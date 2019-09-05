#--- to check if ann item exits in a tuple we use in 
thistuple = ('Mac', 'Elitone', 'Dell', 'HP')
if 'Dell' in thistuple:
    print('Yes, Dell is in thistuple')

#--- to repett an item we use *
thistuple1 = ('Salam',) * 4
print(thistuple1)

#--- to add two tuples or more into one we use +
thistuple2 = (23,5,8,1,34)
thistuple3 = (12,45,3)
thistuple4 = thistuple2 + thistuple3
print(thistuple4)

x = (2,3,4,5)
x = x + (1,2,3)
print(x)

#--- we use len()to the length of a tuple
print(len(thistuple))

#--- we can make a tuple by useing tuple()
y = tuple(('F1', 'F2', 'F3', 'F4'))
print(y)

thislist = [12, 5, -2, 'Dubai', 'B']
thistuple = tuple((thislist))
print(thistuple)

#--- tuple methods
u = thistuple2.count(5)
print(u)

z = thistuple2.index(8)
print(z)