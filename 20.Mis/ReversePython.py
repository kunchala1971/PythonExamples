#take input and print reverse and sum
Number = int(input("Please Enter any Number: "))
#789
Reverse = 0
sum=0
while (Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    sum=sum+Reminder
    Number = Number // 10

print("\n Reverse of entered number is = %d" % Reverse)
print("\n Sum of Entered number is = %d" % sum)



