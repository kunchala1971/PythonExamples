# vehicle={
#         "model" : "Hero",
#         "price" : "45600",
#         "year" : "2010"
#       }
vehicle={"model" : "Hero","price" : "45600","year" : "2010"}
x = vehicle["model"] #it gets value of model key through index
print(x)
print("")
x = vehicle.get("model")# it gets value of model key through method
print(x)
print("")
vehicle["year"] = 2023
#it prints keynames
for key in vehicle:
    print(key)
print("")
#it prints values
for key in vehicle:
    print(vehicle[key])
print("")
# if you want to direct values through loop
for value in vehicle.values():
    print(value)
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
myvehicle=vehicle.copy()
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
for key, value in myvehicle.items():
    print(key, value)