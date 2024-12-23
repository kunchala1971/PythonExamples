#Record Updated
import mysql.connector as conn
mydb =conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
movie_name=(input("Enter Movie Name"))
movie_actress_name=input("Enter Actress Name")
sql = "UPDATE listofmovies SET actress_name = '" \
      + movie_actress_name + "' WHERE movie_name='" + movie_name + "'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")