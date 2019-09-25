#--- lambda function ised inside another function 
def myfunc(x) :
    return lambda a : a * x
mydoubler = myfunc(2)
print(mydoubler(12))
print(mydoubler(11))
print(mydoubler(10))
def myfunc(x) :
    return lambda a : a * x
mytripler = myfunc(3) #triple
print(mytripler(12))
print(mytripler(11))
print(mytripler(10))

def myfunc(x) :
    return lambda a : a * x
mydoubler = myfunc(2) #we can use them both
mytripler = myfunc(3) 
print(mydoubler(12))
print(mydoubler(11))
print(mydoubler(10))
print(mytripler(12))
print(mytripler(11))
print(mytripler(10))