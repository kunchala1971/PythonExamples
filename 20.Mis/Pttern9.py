"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
#Code - 1: for any character or number
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#Code - 2: for only special character
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print("^ "*i)
