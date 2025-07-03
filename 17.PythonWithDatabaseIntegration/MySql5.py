#5.Show the existing data
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM listofmovies ")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
