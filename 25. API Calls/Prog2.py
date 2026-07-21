import json
import requests
# response=requests.get("https://jsonplaceholder.typicode.com/users/9")
response=requests.get("https://jsonplaceholder.typicode.com/todos/2")
print(response.status_code)
data=response.json()
for key in data:
    print(key,":",data[key])
