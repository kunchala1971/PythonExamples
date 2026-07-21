#dynamical type casting
fruit_name=input("Enter Fruit Name")
qty=int(input("Enter Qty"))
rate=float(input("Enter Unit Price"))
total_amount=qty*rate
print("Fruit Name " + fruit_name + " Qty " + str(qty) +
      " Unit Price" + str(rate) + " Total Amount is "
      + str(total_amount))
#while calculation only type casting

fruit_name=input("Enter Fruit Name")
qty=input("Enter Qty")
rate=input("Enter Unit Price")
total_amount=int(qty)*float(rate)
print("Fruit Name " + fruit_name + " Qty " + qty
      + " Unit Price" + rate + " Total Amount is "
      + str(total_amount))