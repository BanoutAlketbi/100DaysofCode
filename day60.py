import json
days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wenesday", "Thursday", "Friday")
print("Tuple: " , days)
tostr = json.dumps(days)
print("String using json: " , tostr)
