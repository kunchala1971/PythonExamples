cumAmount=0
amount=int(input("Enter Amount"))
while amount>0:
    cumAmount+=amount
    print("Live Balance is ",cumAmount)
    amount=int(input("Enter amount"))
else:
    print("Final Balance is ",cumAmount)

