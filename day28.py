#--- while loop
x = 2
while x < 8:
    print(x)
    x += 1 #--- a must otherwise the loop won't end
#--- break a loop
x = 1
while x < 4:
    print(x)
    if x == 3:
        break #--- we use break to stop a loob even if it is true
    x += 1
#--- continue statment is used to skip an iteration and continue with the next
y = 4
while y < 9:
    y += 1
    if y == 7:
        continue
    print(y)
#--- else statement
fee = 10
while fee < 60:
    print(fee)
    fee += 10
else:
        print('fee costs more than 50')


fee = 70
while fee < 60:
    print(fee)
    fee += 10
else:
        print('fee costs more than 50')