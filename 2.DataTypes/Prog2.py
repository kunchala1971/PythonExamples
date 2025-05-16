#dynamically inputs with type cast
code=int(input("Enter Code"))
name=input("Enter Name")
age=int(input("Enter Age"))
course=input("Enter Course")
fees=float(input("Enter Fees"))
is_active=bool(input("Enter Status (True/False"))
# person_id=9999j
person_id=complex(input("Enter Complex Value"))
#type function return the data type
print(type(code))
print(type(name))
print(type(age))
print(type(course))
print(type(fees))
print(type(is_active))
print(type(person_id))