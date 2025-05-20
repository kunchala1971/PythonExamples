class StudentDetails:
    code=100
    name="SrinivasaRao"
    course="Python"
    def showData(self):
        print(self.code)
        print(self.name)
        print(self.course)
    def insertData(self,code,name,course):
        self.code=code
        self.name=name
        self.course=course

p=StudentDetails()# p is an instance of studentdetails
p.showData()
p.insertData(102,"Kiran","Java")
p.showData()

q=StudentDetails()
q.insertData(101,"Durrga","Python")
q.showData()

p.showData()

y=StudentDetails()
y.showData()