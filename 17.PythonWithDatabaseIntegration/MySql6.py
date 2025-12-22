#find record
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
try:
  #student_name=input("Enter your Students Name")
  sno=input("Enter your slno")
  #sql = "SELECT * FROM students WHERE student_name ='"+ student_name + "'"
  sql = "SELECT * FROM students WHERE sno ="+ sno
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
except:
  print("Record Not Found")
