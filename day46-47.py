class library:
    def __init__(self, shelf, book):
        self.shelf = shelf
        self.book = book
    def print_a(self):
        print("this library has", self.shelf, " shelfs that conatins", self.book, " book")
        
class science_section(library):
    def __init__(self, shelf, book, name):
        super().__init__(shelf, book)
        self.name = name
    def print_a(self):
        print("this scection of the library has", self.shelf, " shelfs that conatins", self.book, " book", "also some", self.name)

x = library(45, 300)
x.print_a()
x = science_section(45, 300, "physics books")
x.print_a()
x.shelf = 4
x.book = 20
x.print_a()
