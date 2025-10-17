import json
import requests
# response=requests.get("https://jsonplaceholder.typicode.com/users/9")
response=requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
data=response.json()
for key in data:
    print(key,":",data[key])
