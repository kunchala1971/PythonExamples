strinput=input("Enter inputs only numbers separated by Dollar").split("$")
print(strinput)
s=0
for i in range(0,len(strinput)):
    s=s+int(strinput[i])
    #s = s + strinput[i]
print(s)
