"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
