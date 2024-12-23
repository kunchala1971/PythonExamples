#2. Create Database Dynamically
import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="DURGA"
)
"""
create database databasename 
"""
try:
  mycursor = mydb.cursor()
  dbname=input("Enter DataBaseName")
  mycursor.execute("CREATE DATABASE " + dbname)
  #bydefault the database name will take automatically lowercase letter
  print("Db Successfully Created")
except:
  print("Db alreay Created")