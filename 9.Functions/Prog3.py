#write a program to print multiple table using functions
def print_multiple_table(n):
    i = 1
    while i <= 10:
        print(n, "X", i, "=", int(n) * i)
        i = i + 1


min=int(input("Enter Lower Value"))
max=int(input("Enter Higher Value"))
for i in range(min,max+1):
    print_multiple_table(i)


