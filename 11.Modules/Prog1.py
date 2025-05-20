import MyModules as MM
a=int(input("Enter any number"))
b=int(input("Enter any number"))
result=MM.add(a,b)
print(result)
c=int(input("Enter any number"))
result=MM.add3(a,b,c)
print(result)
result=MM.area(4.5)
print(result)
result=MM.square(12)
print(result)
MM.greeting("SrinivasRao.K")
n=input("Enter any number")
MM.printtable(int(n))
list=["Apples","Grapes","Banana","Cherry"]
tuples=("Apples","Grapes","Banana","Cherry")
MM.showList(list)
MM.showList(tuples)
n=int(input("Enter any number"))
MM.prime(n)



