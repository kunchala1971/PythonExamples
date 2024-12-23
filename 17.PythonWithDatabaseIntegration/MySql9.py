#drop table
import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
try:
  mycursor = mydb.cursor()
  sql = "DROP TABLE listofmovies"
  mycursor.execute(sql)
  print("Table is Deleted")
except:
  print("Table Does't Existed")