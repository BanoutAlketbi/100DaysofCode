#---classes and objects
class myclass:
    x = 12
print(myclass)
p1 = myclass()
print(p1.x)

class person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
p1 = person('Mia', 23)

print(p1.name)
print(p1.age)