thislist = ['F0', 'F1', 'F2', 'F3', 'F4']
print(thislist[1:4])
print(thislist[1:3])

#--- to check if an item exits or not we use in
if 'F2' in thislist:
    print('Yes, the selected command exits')
if 'F5' in thislist:
    print('No, it does not exit')


#--- to repeat an item we use *
x = ['سلام'] * 7
print(x)

#--- to combine 2 lists or more into one we use +

z = ['Dubai', 'Sharjah']
y = ['Abu Dhabi', 'RAK']
r = z + y
print(r)

num1 = [1, 4,12,4,8,7]
num2 = [10.4, 3.2, 12.5, 1.0]
num3 = num1 + num2
print(num3)