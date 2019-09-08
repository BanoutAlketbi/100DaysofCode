#--- Creating a list with methods 
weather = list(('sunny','windy','rainy','stormy','dry'))
print(weather)

print(len(weather)) #num of items in the list
weather.append('frigid') #adding a new items at the end
print(weather)
print(weather.count('sunny'))
weather.insert(3, 'calm') #adding a new item
print(weather)
weather.pop(0) #deleting an item by specifing index
print(weather)
