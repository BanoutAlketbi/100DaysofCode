x = "python" #--global
def example():
    x = 23
    global y 
    y = 21
    print(x) #local
example()
print(x, y)

z = "py"
def example2():
    global z
    z = "yup"
example2()
print(z)
