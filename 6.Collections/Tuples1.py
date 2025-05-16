#tuple Example
month_names=("Jan","Feb","March","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
print(month_names)
#You can access tuple items by referring to the index number, inside square brackets
print(month_names[1])
print(month_names[4:9])
print(month_names[0:7])
print(month_names[7:])
print(month_names[:8])
#dynamically show the months names

min=int(input("Enter lower value"))
max=int(input("Enter max value"))
print(month_names[min:max+1])

for x in month_names[min:max+1]:
  print(x)
#You can loop through the tuple items by using a for loop.

for x in month_names:
  print(x,end=", "),

print("")
if "Dec" in month_names:
  print("Yes, 'Dec' is in the tuple")
else:
  print("No, Dec is not in the tuple")

#print lengthe of tuple
print(len(month_names))
print(type(month_names))
print(len(month_names[1]))
del month_names

