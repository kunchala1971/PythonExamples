#lambda expression with pass arguments

x = lambda a : a * 10
a=int(input("Enter a Value"))
print(x(a))
x1=x(a)
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

