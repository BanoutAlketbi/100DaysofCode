import re
str = "The weather is rainy today"
x = re.findall("in", str)
print(x)
y = re.findall("windy", str)
print(y)
if (y):
    print("Yes, there is a match")
else:
    print("no match")
x = re.search("\s", str)
print("the first white-space character is located in postion:", x.start())
y = re.findall("windy", str)
print(y)
x = re.split("\s", str)
print(x)