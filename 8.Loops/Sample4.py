#Given number prime or not Check
n=int(input("Enter any number"))
i = 2
cnt = 0
while  i < n:
    if n % i == 0:
        cnt = cnt + 1
        break
    i = i + 1
print (cnt)

if cnt == 0:
    print("Prime")
else:
    print("Not Prime")