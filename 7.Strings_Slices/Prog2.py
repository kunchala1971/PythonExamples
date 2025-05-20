#text formating
Qty=input("Enter Qty")
ItemCode= input("Enter Item Name")
price = input("Enter Price")
strtext= "I want {} pieces of item {} for {} Rupees."
print(strtext.format(Qty,ItemCode,price))
strtext= "I want to pay {2} Rupees for {0} pieces of item {1}."
print(strtext.format(Qty,ItemCode,price))
strtext="I want to pay {0} Rupees for {1} pieces of item {2}."
print(strtext.format(price,ItemCode,Qty))
print(f"I want to pay {price} Rupees for {ItemCode} pieces of item {Qty}")

for i in range(1,61):
    code="ECE2025/"+ str(i)
    print("Dear {}, Please attend class {} onwards".format(code,"04-Apr-2025"))

for i in [1,2,5,7,8]:
    code="ECE2024/"+ str(i)
    print("Dear {}, Please attend class {} onwards".format(code,"04-Apr-2024"))
