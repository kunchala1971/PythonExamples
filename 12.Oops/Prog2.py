# how can access class members out side of the class
from contextlib import nullcontext
class StudentDetails():
    code=nullcontext
    name=nullcontext
    course=nullcontext
    def showStudentDetails(self):
        print("Code:", self.code)
        print("Name:", self.name)
        print("Course:", self.course)

ram=StudentDetails()
ram.code=int(input("Enter code"))
ram.name=input("Enter Name")
ram.course=input("Enter Course")
print("Code:", ram.code)
print("Name:",ram.name)
print("Course:",ram.course)
ram.showStudentDetails()