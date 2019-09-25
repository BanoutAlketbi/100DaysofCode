os = ['windows', 'mac ios', 'linux', 'ubunto']
for x in os: #to show all the array elemnts
    print(x)
os.append('chrome os') #to add a new element
print(os)
os.pop(1) #to remove an elemnt
print(os)
#there's another way to remove an elemnt which is 
os.remove('linux')
print(os)


