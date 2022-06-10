//cd your project directory
create virtual environment
(virtualenv venv)

//activate virtual environment
source venv/bin/activate

//to create requirement.txt file
pip freeze > requirements.txt

//install requirement
pip install -r requirements.txt
pip3 install mysql-connector-python-rf

sudo mysql.server start

// Create Grade Range TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE defult_grade (semester VARCHAR(10), subjectcode VARCHAR(10), section VARCHAR(3), A_min VARCHAR(5), A_max VARCHAR(5), A_students VARCHAR(5), A_minus_min VARCHAR(5), A_minus_max VARCHAR(5) , A_minus_students VARCHAR(5), B_plus_min VARCHAR(5), B_plus_max VARCHAR(5) , B_plus_students VARCHAR(5), B_min VARCHAR(5), B_max VARCHAR(5), B_students VARCHAR(5), B_minus_min VARCHAR(5), B_minus_max VARCHAR(5) , B_minus_students VARCHAR(5), C_plus_min VARCHAR(5), C_plus_max VARCHAR(5), C_plus_students VARCHAR(5), C_min VARCHAR(5), C_max VARCHAR(5) , C_students VARCHAR(5), C_minus_min VARCHAR(5), C_minus_max VARCHAR(5), C_minus_students VARCHAR(5), D_min VARCHAR(5), D_max VARCHAR(5) , D_students VARCHAR(5), F_min VARCHAR(5), F_max VARCHAR(5), F_students VARCHAR(5), I_min VARCHAR(5), I_max VARCHAR(5) , I_students VARCHAR(5), W_min VARCHAR(5), W_max VARCHAR(5), W_students VARCHAR(5), PRIMARY KEY (subjectcode))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE modify_grade (semester VARCHAR(10), subjectcode VARCHAR(10), section VARCHAR(3), A_min VARCHAR(5), A_max VARCHAR(5), A_students VARCHAR(5), A_minus_min VARCHAR(5), A_minus_max VARCHAR(5) , A_minus_students VARCHAR(5), B_plus_min VARCHAR(5), B_plus_max VARCHAR(5) , B_plus_students VARCHAR(5), B_min VARCHAR(5), B_max VARCHAR(5), B_students VARCHAR(5), B_minus_min VARCHAR(5), B_minus_max VARCHAR(5) , B_minus_students VARCHAR(5), C_plus_min VARCHAR(5), C_plus_max VARCHAR(5), C_plus_students VARCHAR(5), C_min VARCHAR(5), C_max VARCHAR(5) , C_students VARCHAR(5), C_minus_min VARCHAR(5), C_minus_max VARCHAR(5), C_minus_students VARCHAR(5), D_min VARCHAR(5), D_max VARCHAR(5) , D_students VARCHAR(5), F_min VARCHAR(5), F_max VARCHAR(5), F_students VARCHAR(5), I_min VARCHAR(5), I_max VARCHAR(5) , I_students VARCHAR(5), W_min VARCHAR(5), W_max VARCHAR(5), W_students VARCHAR(5), PRIMARY KEY (subjectcode))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
--------------------------------------------------------------------------------------------------------------------------------

// Create bscs_meeting table 
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE meeting (meetingnumber VARCHAR(10), semester VARCHAR(10), date DATE, time VARCHAR(20), program VARCHAR(6), venue VARCHAR(100), insertDate DATETIME , PRIMARY KEY (meetingnumber))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
--------------------------------------------------------------------------------------------------------------------------------

// Create Subject TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE subject (subjectcode VARCHAR(7), subjectname VARCHAR(100), section VARCHAR(3), program VARCHAR(6), course_type VARCHAR(50), PRIMARY KEY (subjectcode,section))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
--------------------------------------------------------------------------------------------------------------------------------

// Create Codeshare TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE codeshare (semester VARCHAR(10), subjectcode VARCHAR(7), codeshare_subject VARCHAR(7), section VARCHAR(3))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
--------------------------------------------------------------------------------------------------------------------------------

// Create bscs_committe TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE committee (committee_name VARCHAR(100), committee_role VARCHAR(50), program VARCHAR(6))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Create metting_committe TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE meeting_committee (committee_name VARCHAR(100), committee_role VARCHAR(50), program VARCHAR(6))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Create Secretary table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE secretary (username VARCHAR(50), password VARCHAR(20)")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Create offered_subject TABLE
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE offered_subject (semester VARCHAR(10), subjectcode VARCHAR(10), program VARCHAR(6), approved BOOLEAN, changed BOOLEAN, modified BOOLEAN, PRIMARY KEY (semester,subjectcode))")
mydb.commit()
print(mycursor.rowcount, "table created successfully")
--------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------

//insert into graderange
mycursor = mydb.cursor()
sql = "INSERT INTO graderange (semester, subjectcode, section, A_min, A_max, A_minus_min, A_minus_max, B_plus_min, B_plus_max, B_min, B_max, B_minus_min, B_minus_max, C_plus_min, C_plus_max, C_min, C_max, C_minus_min, C_minus_max, D_min, D_max, F_min, F_max, I_min, I_max, W_min, W_max ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s )"
val = [
  ('1/2022', 'DA 1121', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 1001', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 1001', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 2008', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 2101', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 2004', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 2004', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 3436', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'IT 3111', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'IT 4314', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 3007', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 3414', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 4102', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'IT 1251', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 3003', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 4401', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 3449', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 4203', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 4203', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 3008', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 3412', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 4105', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'DA 2101', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 2002', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 2002', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'DA 2103', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 2003', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 2003', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'IT 4291', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'IT 4292', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 3009', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'ITX 3010', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 3200', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CS 4200', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 3010', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
  ('1/2022', 'CSX 3011', '541', '80','100','75','79','70','74','65','69','60','64','55','59','50','54','45','49','40','44','0','39','-','-','-','-'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
--------------------------------------------------------------------------------------------------------------------------------

//insert into subject
mycursor = mydb.cursor()
sql = "INSERT INTO subject (subjectcode, subjectname, section, program, course_type) VALUES (%s, %s, %s, %s, %s)"
val = [
   ('DA 1121', 'Basic Mathematics and Statistics', '541', 'IT', 'Subject'),
  ('ITX 1001', 'Basic Mathematics and Statistics','541', 'IT', 'Subject'),
  ('CSX 1001', 'Basic Mathematics and Statistics','541', 'CS', 'Subject'),
  ('CSX 2008', 'Mathematics Foundation for Computer Science','541', 'CS', 'Subject'),
  ('CS 2101', 'Mathematics Foundation for Computer Science', '541','CS', 'Subject'),
  ('ITX 2004', 'UI/UX Design and Prototyping','541', 'IT', 'Subject'),
  ('CSX 2004', 'UI/UX Design and Prototyping','541', 'CS', 'Subject'),
  ('CS 3436', 'UI/UX Design and Prototyping', '541','CS', 'Subject'),
  ('IT 3111', 'User Interface Design', '541','IT', 'Subject'),
  ('IT 4314', 'Software Engineering Concepts', '541','IT', 'Subject'),
  ('ITX 3007', 'Software Engineering','541', 'IT', 'Subject'),
  ('CS 3414', 'Software Engineering','541', 'CS', 'Subject'),
  ('CSX 4102', 'Software Engineering', '541','CS', 'Subject'),
  ('IT 1251', 'Business Systems','541', 'IT', 'Subject'),
  ('ITX 3003', 'Business Systems', '541','IT', 'Subject'),
  ('CSX 4401', 'Business Systems','541', 'CS', 'Subject'),
  ('CS 3449', 'Machine Learning', '541','CS', 'Subject'),
  ('CSX 4203', 'Machine Learning', '541','CS', 'Subject'),
  ('ITX 4203', 'Machine Learning', '541','IT', 'Subject'),
  ('ITX 3008', 'IT Project Management','541', 'IT', 'Subject'),
  ('CS 3412', 'ICT Project Management','541', 'CS', 'Subject'),
  ('CSX 4105', 'IT Project Management', '541','CS', 'Subject'),
  ('DA 2101', 'Calculus I','541', 'IT', 'Subject'),
  ('ITX 2002', 'Calculus', '541','IT', 'Subject'),
  ('CSX 2002', 'Calculus','541', 'CS', 'Subject'),
  ('DA2103', 'Principles of Statistics', '541','IT', 'Subject'),
  ('ITX 2003', 'Principles of Statistics', '541','IT', 'Subject'),
  ('CSX 2003', 'Principles of Statistics', '541','CS', 'Subject'),
  ('IT 4291 ', 'Senior Project I', '541','IT', 'Project'),
  ('IT 4292', 'Senior Project II', '541','IT', 'Project'),
  ('ITX 3009 ', 'Senior Project I', '541','IT', 'Project'),
  ('ITX 3010', 'Senior Project II', '541','IT', 'Project'),
  ('CS 3200', 'Senior Project I', '541','CS', 'Project'),
  ('CS 4200', 'Senior Project II', '541','CS', 'Project'),
  ('CSX 3010', 'Senior Project I', '541','CS', 'Project'),
  ('CSX 3011', 'Senior Project II', '541','CS', 'Project'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
--------------------------------------------------------------------------------------------------------------------------------

// insert into meeting table
mycursor = mydb.cursor()
sql = "INSERT INTO meeting (semester, subject, date, time, place) VALUES (%s, %s, %s, %s, %s)"
val = ("1/2021", "Meeting", "2021-11-20", "10:30-AM", "MS Team")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
--------------------------------------------------------------------------------------------------------------------------------

// insert into committee table for cs
mycursor = mydb.cursor()
sql = "INSERT INTO committee (committee_name, committee_role, program) VALUES (%s, %s, %s)"
val = [
   ('Dr. Songsak Channarukul', 'Chairperson', 'CS'),
   ('A. Suparwat Charoenvikrom', 'Member', 'CS'),
   ('Asst.Prof.Dr. Benjawan Srisura', 'Member', 'CS'),
   ('A. Pawut Satitsuksanoh', 'Member', 'CS'),
   ('A. Piyakul Tillapart', 'Member', 'CS'),
   ('MS. Chonticha Roongruang', 'Secretary', 'CS'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
--------------------------------------------------------------------------------------------------------------------------------

// insert into committee table for IT
mycursor = mydb.cursor()
sql = "INSERT INTO committee (committee_name, committee_role, program) VALUES (%s, %s, %s)"
val = [
   ('Dr. Songsak Channarukul', 'Chairperson', 'IT'),
   ('A. Suparwat Charoenvikrom', 'Member', 'IT'),
   ('Asst.Prof.Dr. Benjawan Srisura', 'Member', 'IT'),
   ('A. Pawut Satitsuksanoh', 'Member', 'IT'),
   ('A. Piyakul Tillapart', 'Member', 'IT'),
   ('MS. Chonticha Roongruang', 'Secretary', 'IT'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
--------------------------------------------------------------------------------------------------------------------------------

//insert into offered_course
sql = "INSERT INTO offered_course (semester, subjectcode, subjectname, program) VALUES (%s, %s, %s, %s)"
val = [
   ('1/2022', 'IT4314', 'Software Engineering Concepts', 'IT'),
  ('2/2021', 'CS3414', 'Software Engineering', 'CS'),
  (1/2022', 'CSX4102', 'Software Engineering', 'CS'),
  ('2/2021', 'ITX3007', 'Software Engineering', 'IT'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

--------------------------------------------------------------------------------------------------------------------------------
mycursor = mydb.cursor()
sql = "INSERT INTO bscs_meeting (meetingnumber, semester, date, time, program, venue) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("001", "1/2022", "2022-1-1","10:00 AM", "CS", "MS Team")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


 sharecode_result1 = [str(i) for i in sharecode_result]
        sharecode_result2 = list(map(lambda sub:int(int(''.join([ele for ele in sub if ele.isnumeric()]))), sharecode_result1))
        sharecode_result3 = str(sharecode_result2[0:3])
        print(str(sharecode_result3))

