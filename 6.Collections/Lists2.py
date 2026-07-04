#take n elemens and print origianl,sorted,reverse order
items=[]
n=int(input("How much Items you want to Create"))
for x in range(1,n+1):
    element=input("Enter Item Name")
    items.append(element)
    # items.append(input("Enter Item Name"))
print("Original Data")
for x in items:
    print(x)
items.sort()
print("Sorted Data")
for x in items:
    print(x)
items.reverse()
print("Reverse Data")
for x in items:
    print(x)

