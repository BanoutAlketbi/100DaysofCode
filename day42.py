#---methods
class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('Hello my name is ' + self.name)
p1 = person('Adam', 23)
p1.myfunc()
p1.age = 23 #modifying an object
print(p1.age)
del p1.age #to delete the age porperty
del p1 #to delete p1 object
