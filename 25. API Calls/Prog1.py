import json

import requests
#before run theis program we should install the following package
#pip install requests
#response=requests.get("https://jsonplaceholder.typicode.com/users")
response=requests.get("https://jsonplaceholder.typicode.com/comments")
print(response.status_code)
data=response.json()
# x=json.dumps(data,indent=4)
# print(x)

for row in data:
    for key in row:
        print(key,":",row[key])
    print("-"*80)