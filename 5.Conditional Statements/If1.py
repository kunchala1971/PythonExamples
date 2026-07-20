m=int(input("Enter maths marks"))
p=int(input("Enter Phy marks"))
c=int(input("Enter Che marks"))
avg=(m+p+c)/3
if m>34 and p>34 and c>34:
    if 34 < avg < 50:
        print("Ordinary")
    elif 50 <= avg < 60:
        print("Second")
    elif 60 <= avg < 75:
        print("First")
    elif 75 <= avg <= 100:
        print("Distinction")
    else:
        print("Something going wrong")

else:
    if m<35 : print("Maths Failed ",m)
    if p<35 : print("Phy Failed",p)
    if c<35 : print("Che Failed",c)