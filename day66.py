quantity = 5
itemno = 231
price = 23
myorder = "I want {0} pieces of item number {1} for {2:.2f} dirhams."
print(myorder.format(quantity, itemno, price))
#----
age = 34
name = "adam"
txt = "his name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#----
myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "ford", model = "Mustang"))