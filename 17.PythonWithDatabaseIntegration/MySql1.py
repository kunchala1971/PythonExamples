#check mysql is existing or not in specified user
#before run this program must be install xampp
#we must install mysql_connector using the following command in terminal
#pip install mysql_connector

import mysql.connector as conn
try:
  mydb = conn.connect(
    host="localhost",#server name127.0.0.1
    user="root", # by default my sql user name is root and password is blank
    passwd="DURGA", # if password is exists enter password otherwise no need
    port="3306"
  )
  print(mydb)
except:
  print("Connection not Established")
else:
  print("Connection is Ready")