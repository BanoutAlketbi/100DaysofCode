import re #-- I used the re packege to use re.sub function
san = 5
doun = 7
up = 'a'
x = 'Please, I want {} sandwishes and {} dounts'
x = re.sub(up, up.upper(), x) #-- re.sub to replace substrings and in this case it is a
print(x.replace('I', 'we').format(san, doun))