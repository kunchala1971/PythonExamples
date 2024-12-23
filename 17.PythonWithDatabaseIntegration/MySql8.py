#Delete Record
import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
slno=input("Enter Movie Sl No")
sql = "DELETE FROM listofmovies WHERE sno=" + slno
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")