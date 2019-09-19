#--- creating a function
def my_function():
    print('hi from a function')

my_function() #--- calling a function
#--- parameters
def my_function(CTI):
    print(CTI + ' ' + 'IT')
my_function('NET')
my_function('SEC')
my_function('SWC')
my_function('ENT')

#--- Default parameter values
def my_function(city = 'Dubai'):
    print('I live in' + ' ' + city)

my_function('AD')
my_function('Shj')
my_function('Ajman')
my_function()
my_function('Alain')
