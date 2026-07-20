#Record Updated
import mysql.connector as conn
mydb =conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="KKCC"
)
mycursor = mydb.cursor()
course=(input("Enter course"))
student_name=input("Enter student name")
sql = "UPDATE students SET course = '" \
      + course + "' WHERE student_name='" + student_name + "'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")