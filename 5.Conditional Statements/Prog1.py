#conditional statements
#if condition
#then if branch of statements executed
#else
#then else branch of statements executed
#ultimately any one branch can only executed

m=int(input("Enter maths marks"))
p=int(input("Enter Phy marks"))
c=int(input("Enter Che marks"))
if (m > 34 and p > 34 and c > 34):
    print("pass")
else:
    print("Fail")