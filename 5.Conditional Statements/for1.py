# n=int(input("Enter any number"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)
"""
*
**
***
**
*
"""
# n=int(input("Enter any number"))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*" * i)

"""
A
BB
CCC
DDDD
"""
n=int(input("Enter any number"))
for i in range(1,n+1):
    print(chr(96+i)*i)