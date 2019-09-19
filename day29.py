#--- for loop
os = ['windows', 'mac ios', 'linux']
for x in os:
    print(x)

#--- looping through a string
for x in 'python':
    print(x)

#--- break statment
os = ['windows', 'mac ios', 'linux']
for x in os:
    print(x)
    if x == 'mac ios':
        break
os = ['windows', 'mac ios', 'linux']
for x in os:
    if x == 'mac ios':
        break
        print(x) #--- it'll stop after printing windows

#--- continue statment
os = ['windows', 'mac ios', 'linux']
for x in os:
    if x == 'linux':
        continue
        print(x)