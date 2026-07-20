#5.Show the existing data
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="KKCC"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students ")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
