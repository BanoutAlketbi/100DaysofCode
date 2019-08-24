x = 1 # int
y = 3.4 # float
z = 4J # complex
 
print (type(x))
print (type(y))
print (type(z))

#------int

q = 1 # int
w = 299383838383 # int
e = -121 # int

print (type(q))
print (type(w))
print (type(e))

#---float num with a decimal either + or -

r = 2.30 # float
t = 4.0 # float
u = -34.56 # float

print (type(r))
print (type(t))
print (type(u))

# float with power of 10 with an e
 
i = 2E4 # float
o = 34.4e2 # float
p = 6E4 # float
 
print (type(i))
print (type(o))
print (type(p))
 
#complex ends with a J 
 
a = 56+3j # complex 
s = 7j # complex
d = -12j # complex 
 
print (type(a))
print (type(s))
print (type(d))

#----converting using float() int() complex()
f = 23 # int
g = -1.5 # float
h = 5j # complex

# convert from int to float 
q = float(f)
#convert from float to int
w = int(g) 
#convert from int to complex
z = complex(f)
#convert from float to complex 
x = complex(g)

print(q)
print(w)
print(z)
print(x)

print(type(q))
print(type(w))
print(type(z))

# random func to make random num

import random 
print (random.randrange(2,8))
print (random.randrange(2,8))

 


