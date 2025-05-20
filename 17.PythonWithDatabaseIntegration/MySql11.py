#11. Drop  Database Dynamically
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="",
)
"""
drop database databasename 
"""
try:
  mycursor = mydb.cursor()
  dbname=input("Enter DataBaseName")
  mycursor.execute("drop DATABASE " + dbname)
  #bydefault the database name will take automatically lowercase letter
  print("Db Successfully deleted")
except:
  print("Db alreay Deleted")