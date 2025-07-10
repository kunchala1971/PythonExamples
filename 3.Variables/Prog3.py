#dynamical type casting
froot_name=input("Enter Froot Name")
qty=int(input("Enter Qty"))
rate=float(input("Enter Unit Price"))
total_amount=qty*rate
print("Froot Name " + froot_name + " Qty " + str(qty) +
      " Unit Price" + str(rate) + " Total Amount is "
      + str(total_amount))

#while calculation only type casting

froot_name=input("Enter Froot Name")
qty=input("Enter Qty")
rate=input("Enter Unit Price")
total_amount=int(qty)*float(rate)
print("Froot Name " + froot_name + " Qty " + qty
      + " Unit Price" + rate + " Total Amount is "
      + str(total_amount))