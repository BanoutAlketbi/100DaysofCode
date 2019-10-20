import re
txt = "data is the new oil"
x = re.findall("data", txt)
if (x):
    print("the word (data) was found")
else:
    print("None")
    