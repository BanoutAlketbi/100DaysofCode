price = 49
txt = "the price is {} dollars"
print(txt.format(price))
#----
price = 49
txt = "the price is {:.2f} dollars"
print(txt.format(price))
#----
quantity = 3
itemno = 234
price = 48
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))