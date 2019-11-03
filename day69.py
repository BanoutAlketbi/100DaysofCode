
x = open("/Users/banoot/Desktop/test.txt")
x = open("/Users/banoot/Desktop/test.txt", "r")
print(x.read())
x.close()
#-----
f = open("/Users/banoot/Desktop/test.txt", "r")
print(f.read(3))
#----
f = open("/Users/banoot/Desktop/test.txt", "r")
print(f.readline())
print(f.readline())
#---
f = open("/Users/banoot/Desktop/test.txt", "r")
for x in f:
    print(x)
f.close()
