class StudentDetails:
    code=100
    name="Venkat"
    course="CSE"
    def showData(self):
        print("Code :",self.code)
        print("Name:",self.name)
        print("Course:",self.course)
    def insertData(self,code,name,course):
        self.code=code
        self.name=name
        self.course=course

sri=StudentDetails()
sri.showData()
code=int(input("Enter Student Code"))
name=input("Enter Name")
course=input("Enter Course")
sri.insertData(code,name,course)
sri.showData()

ram=StudentDetails()
ram.showData()
ram.insertData(102,"Vasu","Java")
ram.showData()

