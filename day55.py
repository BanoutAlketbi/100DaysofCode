import json
#---from json to py
x = '{ "name": "adam", "age":21, "city":"NY"}'
y = json.loads(x)
print(y["city"]) 
#---from py to json
x = {
    "name": "John",
    "age": 21,
    "city": "chicago"

}
y = json.dumps(x)
print(y)

print(json.dumps("hi"))
print(json.dumps(21))
