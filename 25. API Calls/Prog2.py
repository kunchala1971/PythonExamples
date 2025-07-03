import json
import requests
response=requests.get("https://jsonplaceholder.typicode.com/users/2")
#response=requests.get("https://jsonplaceholder.typicode.com/todoss")
print(response.status_code)
data=response.json()
for key in data:
    print(key,":",data[key])
