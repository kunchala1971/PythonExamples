#Argumnets pass and return value
def sum_of_numbers(num):
    s=0
    for i in num:
        s=s+i
    return s

n=int(input("Enter n value"))
nums=[]
for i in range(1,n+1):
    element=int(input("Enter any number"))
    nums.append(element)

print("The Above List sum  is ",sum_of_numbers(nums))
