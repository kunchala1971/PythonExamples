#Record Updated
import mysql.connector as conn
mydb =conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
director_name=(input("Enter Directory Name"))
movie_name=input("Enter Movi Name")
sql = "UPDATE listofmovies SET director_name = '" \
      + director_name + "' WHERE movie_name='" + movie_name + "'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")