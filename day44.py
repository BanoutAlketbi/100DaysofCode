class computer:
    def __init__(self, cbrand, cyear):
        self.brand = cbrand
        self.year = cyear
    def printname(self):
        print(self.brand, self.year)
        
class laptop(computer):
    def __init__(self, cbrand, cyear, o_s):
        super().__init__(cbrand, cyear)
        self.os = o_s

    def machine_details(self):
        print("this machine is", self.brand, self.year, "and its os is", self.os)
x = laptop("HP", '2019', "windows")
x.machine_details()
