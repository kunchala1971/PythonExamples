import json

import requests

# response=requests.get("https://jsonplaceholder.typicode.com/users")
response=requests.get("https://jsonplaceholder.typicode.com/todos")
print(response.status_code)
data=response.json()
# x=json.dumps(data,indent=4)
# print(x)

for data in data:
    for key in data:
        print(key,":",data[key])
    print("-"*80)