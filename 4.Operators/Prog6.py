#ternary Operator
age=17
if age >= 18:
    message="Eligible"
else:
    message="Not Eligible"

print(message)
#or
message="Eligible" if age>=18 else "Not Eligible"

print(message)
print("Eligible" if age>=16 else "Not Eligible")

