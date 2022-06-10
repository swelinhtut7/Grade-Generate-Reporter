import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krishna123",
    database="gradegenerator"
)


""" mycursor = mydb.cursor()

sql = "DELETE FROM offered_course WHERE subjectcode = 'CS3432'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted") """

""" mycursor = mydb.cursor()

sql = "DROP TABLE meeting"

mycursor.execute(sql)  """

""" mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)  """

""" mycursor = mydb.cursor()  

mycursor.execute("SELECT * FROM meeting_committee")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)  """
  
mycursor = mydb.cursor()
sql = "INSERT INTO meeting_committee (committee_name, committee_role, program) VALUES (%s, %s, %s)"
val = [
   ('Dr. Songsak Channarukul', 'Chairperson', 'CS'),
   ('A. Suparwat Charoenvikrom', 'Member', 'CS'),
   ('Asst.Prof.Dr. Benjawan Srisura', 'Member', 'CS'),
   ('A. Pawut SatCSsuksanoh', 'Member', 'CS'),
   ('A. Piyakul Tillapart', 'Member', 'CS'),
   ('MS. Chonticha Roongruang', 'Secretary', 'CS'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
  





