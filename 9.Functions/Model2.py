# 2)Arguments pass but no return values
def show_welcome_message(msg):
    print("Welcome to " + msg)

input_string=input("Enter Student Name")
show_welcome_message(input_string)


def calculate_area(r):
    area=3.1416*r*r
    print(r," area is ",area)

radius=float(input("Enter radius value"))
calculate_area(radius)
radius=float(input("Enter radius value"))
calculate_area(radius)
radius=float(input("Enter radius value"))
calculate_area(radius)