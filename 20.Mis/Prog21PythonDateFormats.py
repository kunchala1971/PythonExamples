import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%A")) #Return  name of weekday in full form
print(x.strftime("%a")) #Return name of weekday short form
print(x.strftime("%B"))  #returns name of the month Full form
print(x.strftime("%b"))  #returns name of the month short form
print(x.strftime("%w")) #returns now week day 0-6
print(x.strftime("%d")) # returns day of month
print(x.strftime("%m")) # returns month number
print(x.strftime("%Y")) #Year full form
print(x.strftime("%y")) #Year full Shortform
print(x.strftime("%H")) # return hours 24 hours format
print(x.strftime("%I")) # returns 12 hours format
print(x.strftime("%M")) # returns Minutes
print(x.strftime("%S")) # returns Seconds
print(x.strftime("%p")) # return AM/PM
print(x.strftime("%f")) # returns Milliseconds
print(x.strftime("%j")) # Returns day of year
print(x.strftime("%U"))# returns week number of year
print(x.strftime("%c")) # returns local datetime
print(x.strftime("%x")) # local version of date
print(x.strftime("%X")) #local version of time
