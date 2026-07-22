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

Advantages:
1)Re Usability
2)It Uses the Same memory
3)It Reduce the program size
4)It increase the efficiency of the program
"""

#1)No arguments pass and no return values
def show_message():
  print("Hello How are you")

show_message()


def calculate_area():
    r=float(input("Enter radius value"))
    area=3.1416*r*r
    print(r," area is ",area)

calculate_area()
calculate_area()
calculate_area()