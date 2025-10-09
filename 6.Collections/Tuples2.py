#Using the Tuples get month and week names full/short
month_names_short=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
month_names_full=("January","February","March","Apr","May","Jun","Jul","August","September","October","November","December")
week_names_full=("Sunday","Monday","TuesDay","WednesDay","ThursDay","Friday","SaturDay")
week_names_short=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
m=int(input("Enter your Month Number"))
print("Month Short Form :" + month_names_short[(m-1)])
print("Month Full Form :" + month_names_full[(m-1)])

w=int(input("Enter your Week Number"))
print("Week Short Form :" + week_names_short[(w-1)])
print("Week Full Form :" + week_names_full[(w-1)])

