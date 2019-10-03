mytuple = ('HP', "Dell", "Sony")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mystr = 'sony'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

for x in mystr:
    print(x)
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = numbers()
myiter = iter(myclass)
for x in myiter:
    print(x)