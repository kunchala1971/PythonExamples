import json #JavaScript Object Notation
#string
x = '{ "name":"John", "age":30, "city":"New York"}'
print(type(x))
# parse string to object
y = json.loads(x)
print(type(y))
# the result is a Python dictionary:
print(y["age"])
print(y["name"])
print(y["city"])
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(type(x))
# convert into JSON string:
y = json.dumps(x)
# the result is a JSON string:
print(type(y))
print(y)

z=json.loads(y) # string to object
print(z["name"])