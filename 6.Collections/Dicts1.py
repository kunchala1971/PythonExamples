# vehicle={
#         "model" : "Hero",
#         "price" : "45600",
#         "year" : "2010"
#       }
vehicle={"model" : "Hero","price" : 45600,"year" : 2010}
x = vehicle["model"] #it gets value of model key through index
print(x)
x = vehicle.get("model")# it gets value of model key through method
print(x)

vehicle["year"] = 2026
#it prints keynames
for el in vehicle:
    print(el)
print("")
#it prints values
for el in vehicle:
    print(vehicle[el])
    print(vehicle.get(el))
print("")
# if you want to direct values through loop
for el in vehicle.values():
    print(el)
print("")
#if you want to key and values
for key, value in vehicle.items():
    print(key, value)
print("")
if "model" in vehicle:
    print("Yes, 'model' is one of the key")
print("")
# you can also add key and values in dictionaries
vehicle["color"] = "blue"
for key, value in vehicle.items():
    print(key, value)
print("")
#copy one dictionary to another dictionary
MyVehicle=vehicle.copy()
# you can also remove the key and values
vehicle.pop("model")
for key, value in vehicle.items():
    print(key, value)
print("")
# it removes last added item
vehicle.popitem()
for key, value in vehicle.items():
    print(key, value)
print("")
# it removes the complete dictionary
#del dicts
#or
vehicle.clear()
print("")
print("My Vehicle Details")
for key, value in MyVehicle.items():
    print(key, value)