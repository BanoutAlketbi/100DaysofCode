#---parent class
class computer:
    def __init__(self, cbrand, cyear):
        self.brand = cbrand
        self.year = cyear
    def printname(self):
        print(self.brand, self.year)
x = computer('HP', 2015)
x.printname()
class laptop(computer): #child class
    pass 
y = laptop('Dell', 2016) 
y.printname()
#__init__ function for child class(it will overrides the parent's __init__ when used)
class laptop(computer):
    def __init__(self, cbrand, cyear):
        computer.__init__(self, cbrand, cyear)
z = laptop('Sony', 2017)
z.printname()