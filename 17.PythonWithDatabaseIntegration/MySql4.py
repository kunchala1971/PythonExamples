#4. How to insert the data
import mysql.connector as conn
try:
  mydb = conn.connect(
    host="localhost",
    user="root",
    passwd="DURGA",
    database="KKCC"
  )
  """
  insert into tablename(column1,column2) values(column1value,column2value)
  """
  mycursor = mydb.cursor()
  sql = "INSERT INTO listofmovies (sno,movie_name,hero_name,actress_name," \
        "director_name,realease_year) VALUES (%s, %s, %s ,%s, %s, %s)"
  sno=input("Enter your sno")
  movie_name=input("Enter your movie_name")
  hero_name=input("Enter your hero_name")
  actress_name=input("Enter your actress_name")
  director_name=input("Enter your director_name")
  realease_year=input("Enter your realease_year(yyyy-mm-dd")
  val = (sno,movie_name,hero_name,actress_name,director_name,realease_year)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
except:
  print("Inserting Fail")