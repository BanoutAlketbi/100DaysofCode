import re
txt = "The weather is nice"
x = re.sub("\s", "9", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)
x = re.search("ea", txt)
print(x)
x = re.search(r"\bT\w+", txt)
print(x.span())
x = re.search(r"\bT\w+", txt)
print(x.string)
x = re.search(r"\bT\w+", txt)
print(x.group())
