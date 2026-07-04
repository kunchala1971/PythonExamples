#text formating
Qty=input("Enter Qty")
ItemCode= input("Enter Item Name")
price = input("Enter Price")
strtext= "I want {} pieces of item {} for {} Rupees."
print(strtext.format(Qty,ItemCode,price))
print(f"I want to pay {price} Rupees for {ItemCode} pieces of item {Qty}")


for i in range(1,61):
    code="ECE2026/"+ str(i)
    print(f"Dear {code}, Please attend class {'24-Jun-2026'} onwards")

for i in [1,2,5,7,8,11]:
    code="ECE2024/"+ str(i)
    print("Dear {}, Please attend class {} onwards".format(code,"24-Apr-2026"))
