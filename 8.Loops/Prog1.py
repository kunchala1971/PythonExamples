#sample1
for char in 'Python':
    print(char,end=", ")
print("")
for char in "Hello Python How  are you":
     print(char,end=", ")

print("")

for num in "123456":
     print(num,end=", "),
print("")

x=input("Enter a content")
for char in x:
    print(char,end=", ")
print("")

#take n and print 1... n numbers
n=int(input("Enter any number it prints 1..n th number"))
i = 1
while i <=(n):
    print(i)
    i += 1

#Take number and print multiple Table
n=input("Enter any number")
i=1
while i <= 10:
    #print(n , "X" , i , "=" , int(n) * i)
    # print(str(n) + "X" + str(i) + "=" + str(int(n) * i))
    print(f"{n}X{i}={int(n)*int(i)}")
    i = i + 1


#Given number prime or not Check
n=int(input("Enter any number"))
i = 2
cnt = 0
while  i < n:
    if n % i == 0:
        cnt = cnt + 1
    i = i + 1
print (cnt)

if cnt == 0:
    print("Prime")
else:
    print("Not Prime")
