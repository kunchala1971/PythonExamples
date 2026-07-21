"""
What is function ?
A function  is a Separate block of code
How to define the functions in python
def function_name(arg1,arg2):
    ------
    ------
    return (arg)

We can pass no of arguments but it returns only one argument

Types of Functions
1)User Defined Functions (Developer made function)
Different Categories
    1)No Arguments pass No Return value
    2)Arguments pass but No return value
    3)Arguments pass and return value
    4)No Arguments pass but return value

2)Pre-defined functions (System Libraries)
    lower()
    upper()
    strip()
    lstrip()
    rstrip()
"""




#1)No arugments pass and no return values
def show_message():
  print("Hello How are you")

show_message()

# 2)Arguments pass but no return values
def show_welcome_message(input_string):
    print("Welecome to " + input_string)

input_string=input("Enter Student Name")
show_welcome_message(input_string)

#3) arugments pass and return value
def add(a,b,c):
    return (a+b+c)
c=add(45,56,67)
print(c)

#4)Arguments pass but no return values
# (if you are not pass any arguments it takes  default arguments)
def show_home_town(city = "Ongole"):
    print("I am from " + city)

show_home_town()
show_home_town("Tirupathi")
city=input("Enter Your Home City")
show_home_town(city)

#print lists using functions
def show_lists(args):
  for x in args:
    print(x)
fruits = ["apple", "banana", "cherry"]
show_lists(fruits)



a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
print(add(a,b,c))

def welcomeMessage(name):
    print("Welcome to " + name + " Our Program")

strname=input("Enter name")
welcomeMessage(strname)
