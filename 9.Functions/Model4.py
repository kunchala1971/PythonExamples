#No Arguments pass But return value
def calculate_area():
    r=float(input("Enter Radius value"))
    print(r," Area is ",end="  ")
    pi=3.1416
    area=pi*r*r
    return area

area=calculate_area()
print(area)


