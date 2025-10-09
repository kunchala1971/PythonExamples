import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

a=json.loads('{"name": "John", "age": 30}')
print(a)

#Note:Sets cannot works in Json
#print(json.dumps ({1,2,3,4,5}))