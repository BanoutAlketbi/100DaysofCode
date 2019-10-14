import json
x = {
    "name": "adam",
    "age": 23,
    "married": True,
    "divorced": False,
    "children": ("Max", "Sally"),
    "pets": None,
    "cars": [
        {"model": "BMW", "mpg": 34},
        {"model": "ford", "mpg": 23}
    ]
}
print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))