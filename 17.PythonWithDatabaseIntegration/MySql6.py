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
  moviename=input("Enter your movie name")
  # sno=input("Enter your slno")
  sql = "SELECT * FROM listofmovies WHERE movie_name ='"+ moviename + "'"
  # sql = "SELECT * FROM listofmovies WHERE sno ="+ sno
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
except:
  print("Record Not Found")
