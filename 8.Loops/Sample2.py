#take n and print 1... n numbers and print its sum
n=int(input("Enter any number it prints 1..n th number"))
i = 1
sum = 0
while i <= n:
    print(i)
    sum=sum+i
    i += 1
print("Sum of n numbers ",sum)
