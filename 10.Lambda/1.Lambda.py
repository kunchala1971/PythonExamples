#lambda expression with pass arguments
x = lambda a : a * 10
arg1=int(input("Enter a Value"))
print(x(arg1))
x1=x(arg1)
print(x1)

a=int(input("Enter a Value"))
b=int(input("Enter b Value"))
x = lambda a, b : a * b * 10
y=x(a, b)
print(y)
print(x(5,8)) #400

a=int(input("Enter a Value"))
b=int(input("Enter b Value"))
c=int(input("Enter c Value"))
x = lambda a, b, c : a * b + c
print(x(a, b, c))

area=lambda r,pi : pi*r*r
print(area(4.56,3.1416))

