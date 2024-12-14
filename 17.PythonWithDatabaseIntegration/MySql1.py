#check mysql is existing or not in specified user
#before run this program must be install xampp
#we must install mysql_connector using the following command in terminal
#pip install mysql_connector

import mysql.connector as MyConnection
try:
  mydb = MyConnection.connect(
    host="localhost",#server name
    user="root", # by default my sql user name is root and password is blank
    passwd="DURGA", # if password is exists enter password otherwise no need
    port="3306"
  )
  print(mydb)
except:
  print("Connection not Established")
else:
  print("Connection is Ready")