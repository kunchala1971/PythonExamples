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
  sql = "INSERT INTO students (sno ,student_name ,course ,city ,state ,join_date) VALUES (%s, %s, %s ,%s, %s, %s)"
  sno=input("Enter your sno")
  student_name=input("Enter Student Name")
  course=input("Enter  Course")
  city=input("Enter  City")
  state=input("Enter State")
  join_date=input("Enter your Join_Date(yyyy-mm-dd")
  val = (sno,student_name,course,city,state,join_date)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
except:
  print("Inserting Fail")