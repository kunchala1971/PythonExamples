n=int(input("No of Days"))
for i in range(1,n+1):
    d=int(input("Week Day"))
    is_vacation=bool(input("To day is Vacation"))
    if d>=2 and d<=6 and is_vacation==True:
        print("Wakeup on 7 AM")
    elif(d==1 or d==7) and is_vacation==True:
        print("Wakeup on 9 AM")
    elif d>=2 and d<=6 and is_vacation==False:
        print("Wakeup on 5 AM")
    elif (d==1 or d==7) and is_vacation==False:
        print("Wakeup on 6 AM")
    else:
        print("Given Input is Wrong")



