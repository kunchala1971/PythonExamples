#3. create table
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
  database="kkcc"
)
"""
create table tablename(
columnname1 datatype(size),
columnname2 datatype(size),
)
"""
mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE TABLE students "
                   "(sno int(5),student_name varchar(30),"
                   "course VARCHAR(128),"
                   "city VARCHAR(128),"
                   "state varchar(128))")
  print("Table Successfully Created")
except:
  print("Table already Created")