# read n records
import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="KKCC"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM listofmovies order by sno desc LIMIT 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)