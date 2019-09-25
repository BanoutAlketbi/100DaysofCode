def my_function (food) :
    for x in food:
        print(x)

fastf = ['fries', 'burgers', 'pizza']

my_function(fastf)

def my_function (x):
    return 2 * x

print(my_function(2))
print(my_function(6))

#--- Key arguments (kwargs)
def my_function(memb1, memb2, memb3):
    print('The most active member is' +' ' + memb1)

my_function(memb1= 'Adam', memb2='Sally', memb3='Max')
#--- Arbitary Arguments
def my_function(* membs):
    print('The most active member is' +' ' + membs[2])
my_function('Adam', 'Sally', 'Max')

#---Recursion
def fact (num):
        if num == 0 : return 1
        else : return num * fact(num -1)
print(fact(3), fact(2), fact(0))
