#lambda expressions with functions
#Single Argument
def myfunc(n):
  print( " N=",n)
  return lambda a:a*n
x = myfunc(2)
print(x(11))

#output 22
#Multiple Arguments
def myfunc(b,c):
  return lambda a,d : a*b*c*d
y = myfunc(2,3)
print(y(10,5))
#output 300