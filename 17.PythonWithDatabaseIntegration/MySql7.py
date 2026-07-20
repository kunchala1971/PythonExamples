#7. order by name
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="KKCC"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM students ORDER BY sno   " #by default ascending
#sql = "SELECT * FROM students ORDER BY student_name desc "  #descending
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)