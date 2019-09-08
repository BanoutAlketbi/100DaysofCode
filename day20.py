thisset = {} #set is a collection of items that are unorderd and unindxed
print(thisset)

thisset = {'F1', 'F4', 23}
print(thisset)

thisset = {1, 'Apple', 'F4', 1, 45}
print(thisset)

print('F4' in thisset) #to check if an item exits in a set we use in 
thisset.add('Hello') #it allows us to add one item only each time
print(thisset)
thisset.update([23, 5, -1, "Dubai"]) #to add more than 1 item
print(thisset)
