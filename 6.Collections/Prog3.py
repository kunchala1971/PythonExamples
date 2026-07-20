n=int(input("Enter n value"))
items=[]
print("Enter ",n, " Items")
for i in range(1,n+1):
    element=input("Enter Item name")
    items.append(element)

print(items)
#items.clear()
del items
#print(items)