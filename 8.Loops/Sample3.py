#Take number and print multiple Table
n=input("Enter any number")
i=1
while i <= 10:
    print(n , "X" , i , "=" , int(n) * i)
    #print(str(n) + "X" + str(i) + "=" + str(int(n) * i))
    #print(f"{n}X{i}={int(n)*int(i)}")
    i = i + 1