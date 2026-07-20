#Delete Record
import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="KKCC"
)
mycursor = mydb.cursor()
slno=input("Enter  Sl No")
sql = "DELETE FROM students WHERE sno=" + slno
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")