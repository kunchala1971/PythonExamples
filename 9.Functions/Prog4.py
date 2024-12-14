#write a program to print reverse order any collections
def tuple_reverse(arg):
    l=len(arg)
    for i in range(1,l+1):
        print(arg[l-i])

def tuple_adv_reverse(week_days):
    print(week_days[::-1])

week_days=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
#week_days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
tuple_reverse(week_days)
tuple_adv_reverse(week_days)
print("Kunchala Srinivasarao"[::-1])



