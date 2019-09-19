#--- range function
for x in range(8):
    print(x)
for x in range(0,3):
    print(x)
for x in range(2, 10, 2): #--- we specify the increment value by adding a 3d value
    print(x)
#--- else in for loop
for x in range(3):
    print(x)
else:
        print('done')
#--- nested loops 
size1 = ['small', 'medium', 'big'] #---outer loop
food = ['pie', 'fries', 'water'] #--- inner loop

for z in size1:
    for y in food:
        print(z,y)
