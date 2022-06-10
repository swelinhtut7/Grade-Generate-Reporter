import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="krishna123",
  database= "gradegenerator"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)