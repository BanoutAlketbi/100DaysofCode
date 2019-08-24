x = 'apple'
y = 'orange'
z = "liomn"

basket = x +' '+ y + ' '+ z 
print(basket) 
print (basket.split())

n = 6
print([basket[i:i+n] for i in range(0, len(basket), n)])

