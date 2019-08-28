#--- to combine strings and numbers we use format(), it also can take a # of arguments 
street = 7
address = 'I live in Dubai, street number {}'
print(address.format(street))

shirt = 2
jacket = 4
jeans = 2
order = 'I want to get these {} shirts, those {} jackets and these {} jeans. '
print(order.format(shirt, jacket, jeans))

order = 'I want to get these {2} shirts, those {0} jackets and these {2} jeans. '
print(order.format(shirt, jacket, jeans))
