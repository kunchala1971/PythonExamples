#write a program to print prime or not using the functions
def prime_or_not(n):
    i = 2
    cnt = 0
    while i > 1 and i < n:
        if n % i == 0:
            cnt = cnt + 1
        i = i + 1

    if cnt == 0:
        print(n,end=", ")
    # else:
    #     print(n," This is Not Prime")

# n=int(input("Enter any Number"))
# prime_or_not(n)
# n=int(input("Enter any Number"))
# prime_or_not(n)
# n=int(input("Enter any Number"))
# prime_or_not(n)
min=int(input("Enter Lower Value"))
max=int(input("Enter Higher Value"))
for i in range(min,max+1):
    prime_or_not(i)