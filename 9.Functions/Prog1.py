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
