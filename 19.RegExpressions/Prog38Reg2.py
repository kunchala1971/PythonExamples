import re
str = "Welcome To Python Students"
x = re.findall("^Welcome", str)
if (x):
  print("Yes, the string starts with 'Welcome'")
else:
  print("No match")
#Check if the string ends with 'Students':
x = re.findall("Students$", str)
if (x):
  print("Yes, the string ends with 'Students'")
else:
  print("No match")
str = "Hi Students How are You Hai Hima"
#Check if the string contains "Hi" followed by 0 or more "x" characters:
print(str)
x = re.findall("Hi*", str)
print(x)
str = "Hi Students How are You Hai"
#Check if the string contains "H+" followed by 0 or more "x" characters:
x = re.findall("H+", str)
print(x)
str = "Hi Students How are You HH  hai this is testing HHa"
x = re.findall("HH*", str)
print(x)
str = "Hi Students How are You HH!"
#Check if the string contains either "falls" or "stays":
x = re.findall("Hi|How", str)
print(x)
str = "Welcome to Python Students"
x = re.findall("[a-z,WPS]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
str = "Welcome to Python Students"
x = re.split("\s", str) #\s means empty space
print(x)
str = "Welcome to Python Students9"
x = re.sub("\s", "_", str)
print(x)
