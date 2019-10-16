import re
txt = "Abu Dhabi is UAE's capital"
x = re.search("^Abu.*capital$", txt)
if (x):
    print("Yes, it does match!")
else:
    print("There's no match")
y = re.findall(r"^\w+", txt)
print(y)
y = re.findall("\Abu", txt)
print(y)
if (x):
    print("Yes, it does match!")
else:
    print("There's no match")

y = re.findall("[^arn]", txt)
print(y)
if (x):
    print("Yes, there is a match!")
else:
    print("There's no match")