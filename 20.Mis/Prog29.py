def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modof(x,y):
    return(x%y)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
choice=0
try:
    while choice<6 :
        choice = int(input("Enter choice(1/2/3/4/5):"))
        if choice<6:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if choice == 1:
                print(str(num1) +  "+" +  str(num2) + "=" + str( add(num1, num2)))
            elif choice == 2:
                print(num1,"-",num2,"=", subtract(num1,num2))
            elif choice == 3:
                print(num1,"*",num2,"=", multiply(num1,num2))
            elif choice == 4:
                print(num1,"/",num2,"=", divide(num1,num2))
            elif choice==5:
                print(num1, " Mod of ", num2, "=", modof(num1, num2))
        else:
            print("Invalid input")
except:
    print("Something Going Wrong")