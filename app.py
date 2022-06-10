from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Krishna&Lexi'

# Configure for database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'krishna123'
app.config['MYSQL_DB'] = 'gradegenerator'

# Initialize MySQL
mysql = MySQL(app)

# ------------------------------------------------------------------------------------------------------------------------------
#                                                   Login page                                                       
# ------------------------------------------------------------------------------------------------------------------------------

# For Login Page
@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM secretary WHERE username = %s AND password = %s', (username, password,))

        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in database table, allow to access
        if account:
            # Create session data, to access this data in other routes
            session['loggedin'] = True
            session['password'] = account['password']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('BSCS_Meeting'))

        else:
            
            flash('Incorrect username or password!', 'error')
            return render_template('homepage.html')

    return render_template('homepage.html')

# ------------------------------------------------------------------------------------------------------------------------------
#                                                    Commtitte Member                                                         
# ------------------------------------------------------------------------------------------------------------------------------

# >> Computer Science Committe Member<<

#Show BSCS Committe lists
@app.route("/BSCS_Committee_Setup", methods = ["POST", "GET"])
def BSCS_Committee_Setup():
    bscs_committee_all_list = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_committee = cursor.execute("SELECT * FROM committee WHERE program = 'CS'")

    if bscs_committee > 0:
        bscs_committee_all_list = cursor.fetchall()
    else:
        flash("There is no data for BSCS Committee Member!")

    return render_template('bscs_committee_setup.html', bscs_committee_all_list = bscs_committee_all_list)

#Add New BSCS Committe Member
@app.route("/BSCS_Add_Committee", methods = ["POST","GET"])
def BSCS_Add_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        bscs_committe_name = request.form['bscs_committe_name']
        bscs_committe_role = request.form['bscs_committe_role']
        program = 'CS'
               
        cur.execute("INSERT INTO committee (committee_name, committee_role, program) VALUES (%s, %s, %s)",[bscs_committe_name, bscs_committe_role, program])
        mysql.connection.commit()       
        cur.close()
        
        return jsonify()

#Edit BSCS Committe Member
@app.route("/BSCS_Edit_Committee", methods = ["POST","GET"])
def BSCS_Edit_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        bscs_committe_name = request.form['bscs_committe_name']
        bscs_committe_role = request.form['bscs_committe_role']

        cur.execute("UPDATE committee SET committee_name = %s, committee_role = %s WHERE committee_name = %s AND program = 'CS'", [bscs_committe_name, bscs_committe_role, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'
        
        return jsonify(msg)

#Delete BSCS Committe Member
@app.route("/BSCS_Delete_Committee",methods = ["POST","GET"])
def BSCS_Delete_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute("DELETE FROM committee WHERE program = 'CS' AND committee_name = %s",[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg)  

# ------------------------------------------------------------------------------------------------------------------------------

@app.route("/BSCS_Add_Meeting_Committee", methods = ["POST","GET"])
def BSCS_Add_Meeting_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        bscs_committe_name = request.form['bscs_committe_name']
        bscs_committe_role = request.form['bscs_committe_role']
        program = 'CS'
               
        cur.execute("INSERT INTO meeting_committee (committee_name, committee_role, program) VALUES (%s, %s, %s)",[bscs_committe_name, bscs_committe_role, program])
        mysql.connection.commit()       
        cur.close()
        
        return jsonify()

#Edit BSCS Committe Member
@app.route("/BSCS_Edit_Meeting_Committee", methods = ["POST","GET"])
def BSCS_Edit_Meeting_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        bscs_committe_name = request.form['bscs_committe_name']
        bscs_committe_role = request.form['bscs_committe_role']

        cur.execute("UPDATE meeting_committee SET committee_name = %s, committee_role = %s WHERE committee_name = %s AND program = 'CS'", [bscs_committe_name, bscs_committe_role, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'
        
        return jsonify(msg)

#Delete BSCS Committe Member
@app.route("/BSCS_Delete_Meeting_Committee",methods = ["POST","GET"])
def BSCS_Delete_Meeting_Committee():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute("DELETE FROM meeting_committee WHERE program = 'CS' AND committee_name = %s",[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg)  
    
# ------------------------------------------------------------------------------------------------------------------------------

# >> Information Technology Committe Member <<

#Show BSIT Committe lists
@app.route("/BSIT_Committee_Setup", methods = ["POST", "GET"])
def BSIT_Committee_Setup():
    bsit_committee_all_list = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_committee = cursor.execute("SELECT * FROM committee WHERE program = 'IT'")

    if bsit_committee > 0:
        bsit_committee_all_list = cursor.fetchall()
    else:
       flash("There is no data for BSIT Committee Member!")

    return render_template('bsit_committee_setup.html', bsit_committee_all_list = bsit_committee_all_list)

#Add New BSIT Committe Member
@app.route("/BSIT_ADD_Committee", methods = ["POST","GET"])
def BSIT_ADD_Committee():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        bsit_committe_name = request.form['bsit_committe_name']
        bsit_committe_role = request.form['bsit_committe_role']
        program = 'IT'
               
        cur.execute("INSERT INTO committee (committee_name, committee_role, program) VALUES (%s, %s, %s)",[bsit_committe_name, bsit_committe_role, program])
        mysql.connection.commit()       
        cur.close()

        return jsonify()

#Edit BSIT Committe Member
@app.route("/BSIT_Edit_Committee", methods = ["POST","GET"])
def BSIT_Edit_Committee():
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        bsit_committe_name = request.form['bsit_committe_name']
        bsit_committe_role = request.form['bsit_committe_role']

        cur.execute("UPDATE committee SET committee_name = %s, committee_role = %s WHERE committee_name = %s AND program = 'IT'", [bsit_committe_name, bsit_committe_role, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'
        
        return jsonify(msg)

#Delete BSIT Committe Member
@app.route("/BSIT_Delete_Committee", methods = ["POST","GET"])
def BSIT_Delete_Committee():
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute("DELETE FROM committee WHERE program = 'IT' AND committee_name = %s",[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg)  

# ------------------------------------------------------------------------------------------------------------------------------
#                                             Subject & Project List                                                                  
# ------------------------------------------------------------------------------------------------------------------------------

# >> Computer Science Project List <<

# Show BSCS Project lists
@app.route('/BSCS_Project_List', methods = ["POST", "GET"])
def BSCS_Project_List():

    bscs_project_list=''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_data = cursor.execute(
        "SELECT * FROM subject WHERE program = 'CS' AND course_type = 'Project' ORDER BY subjectname ASC")

    if bscs_data > 0:
        bscs_project_list = cursor.fetchall()
    
    if request.method == 'POST' and 'search_subject' in request.form:
        search_subject = request.form['search_subject']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        bscs_data = cursor.execute("SELECT * FROM subject WHERE program = 'CS' AND subjectcode = %s AND course_type = 'Project' ORDER BY subjectname ASC",[search_subject])
        
        if bscs_data > 0:
            bscs_project_list = cursor.fetchall()
            
        else:
            flash('NO DATA FOUND!')
               
    return render_template('bscs_project_list.html', bscs_project_list = bscs_project_list)

# ADD BSCS Project
@app.route("/BSCS_Add_Project", methods = ["POST","GET"])
def BSCS_Add_Project():
    
    if request.method == 'POST' and 'subjectcode' in request.form and 'subjectname' in request.form and 'section' in request.form:
        # Create variables for easy access
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'CS'
        course_type = 'Project'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("New Added Project & Section are Already Existed!")
            return render_template('error.html')

        else:
            
            # Insert new data into itmeeting table
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO subject VALUES (%s, %s, %s, %s, %s)',(subjectcode, subjectname, section, program, course_type,))
            mysql.connection.commit()
            cursor.close()
            msg = 'New record created successfully'
            return jsonify(msg)

# Edit BSCS project 
@app.route("/BSCS_Edit_Project", methods =[ "POST","GET"])
def BSCS_Edit_Project():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        string = request.form['string']
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'CS'
        course_type = 'Project'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("Your's Edited Subject & Section are Already Existed. Please type a different!")
            return render_template('error.html')

        else:
               
            cur.execute("UPDATE subject SET subjectcode = %s, subjectname = %s, section = %s, program = %s, course_type = %s WHERE subjectcode = %s ", [subjectcode, subjectname, section, program, course_type, string])
            mysql.connection.commit()       
            cur.close()
            msg = 'Record successfully Updated'
            
            return jsonify(msg)

# ------------------------------------------------------------------------------------------------------------------------------

# >> Computer Science Subject List <<

#Show BSCS subject lists
@app.route('/BSCS_Subject_List', methods = ["POST", "GET"])
def BSCS_Subject_List():

    bscs_subjects_list=''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_data = cursor.execute(
        "SELECT * FROM subject WHERE program = 'CS' AND course_type = 'Subject' ORDER BY subjectname ASC")

    if bscs_data > 0:
        bscs_subjects_list = cursor.fetchall()
    
    if request.method == 'POST' and 'search_subject' in request.form:
        search_subject = request.form['search_subject']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        bscs_data = cursor.execute("SELECT * FROM subject WHERE program = 'CS' AND subjectcode = %s AND course_type = 'Subject' ORDER BY subjectname ASC",[search_subject])
        
        if bscs_data > 0:
            bscs_subjects_list = cursor.fetchall()
            
        else:
            flash('NO DATA FOUND!')
               
    return render_template('bscs_subject_list.html', bscs_subjects_list = bscs_subjects_list)
    
# ADD BSCS Subject
@app.route("/BSCS_Add_Subject", methods = ["POST","GET"])
def BSCS_Add_Subject():
    
    if request.method == 'POST' and 'subjectcode' in request.form and 'subjectname' in request.form and 'section' in request.form:
        # Create variables for easy access
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'CS'
        course_type = 'Subject'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("New Added Subject & Section are Already Existed!")
            return render_template('error.html')

        else:
            
            # Insert new data into itmeeting table
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO subject VALUES (%s, %s, %s, %s, %s)',(subjectcode, subjectname, section, program, course_type,))
            mysql.connection.commit()
            cursor.close()
            msg = 'New record created successfully'
            return jsonify(msg)

# Edit BSCS subject 
@app.route("/BSCS_Edit_Subject", methods =[ "POST","GET"])
def BSCS_Edit_Subject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        string = request.form['string']
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'CS'
        course_type = 'Subject'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("Your's Edited Subject & Section are Already Existed. Please type a different!")
            return render_template('error.html')

        else:
               
            cur.execute("UPDATE subject SET subjectcode = %s, subjectname = %s, section = %s, program = %s, course_type = %s WHERE subjectcode = %s ", [subjectcode, subjectname, section, program, course_type, string])
            mysql.connection.commit()       
            cur.close()
            msg = 'Record successfully Updated'
            
            return jsonify(msg)
        
# DELETE BSCS Project & Subject
@app.route("/BSCS_Delete_Subject", methods = ["POST","GET"])
def BSCS_Delete_Subject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM subject WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM offered_subject WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM defult_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM modify_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM codeshare WHERE subjectcode = %s',[getid])
        mysql.connection.commit()
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg) 

# ------------------------------------------------------------------------------------------------------------------------------

# >> Information Technology Project List <<

# Show BSIT Project lists
@app.route('/BSIT_Project_List', methods = ["POST", "GET"])
def BSIT_Project_List():

    bsit_project_list=''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_data = cursor.execute("SELECT * FROM subject WHERE program = 'IT' AND course_type = 'Project' ORDER BY subjectname ASC")

    if bsit_data > 0:
        bsit_project_list = cursor.fetchall()
    
    if request.method == 'POST' and 'search_subject' in request.form:
        search_subject = request.form['search_subject']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        bsit_data = cursor.execute("SELECT * FROM subject WHERE program = 'IT' AND subjectcode = %s AND course_type = 'Project' ORDER BY subjectname ASC",[search_subject])
        
        if bsit_data > 0:
            bsit_project_list = cursor.fetchall()
            
        else:
            flash('NO DATA FOUND!')
               
    return render_template('bsit_project_list.html', bsit_project_list = bsit_project_list)

# ADD BSIT Project
@app.route("/BSIT_Add_Project", methods = ["POST","GET"])
def BSIT_Add_Project():
    
    if request.method == 'POST' and 'subjectcode' in request.form and 'subjectname' in request.form and 'section' in request.form:
        # Create variables for easy access
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'IT'
        course_type = 'Project'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("New Added Project & Section are Already Existed!")
            return render_template('error.html')

        else:
            
            # Insert new data into itmeeting table
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO subject VALUES (%s, %s, %s, %s, %s)',(subjectcode, subjectname, section, program, course_type,))
            mysql.connection.commit()
            cursor.close()
            msg = 'New record created successfully'
            return jsonify(msg)

# Edit BSIT project 
@app.route("/BSIT_Edit_Project", methods =[ "POST","GET"])
def BSIT_Edit_Project():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        string = request.form['string']
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'IT'
        course_type = 'Project'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("Your's Edited Subject & Section are Already Existed. Please type a different!")
            return render_template('error.html')

        else:
               
            cur.execute("UPDATE subject SET subjectcode = %s, subjectname = %s, section = %s, program = %s, course_type = %s WHERE subjectcode = %s ", [subjectcode, subjectname, section, program, course_type, string])
            mysql.connection.commit()       
            cur.close()
            msg = 'Record successfully Updated'
            
            return jsonify(msg)

# ------------------------------------------------------------------------------------------------------------------------------

# >> Information Technology Subject List <<

# Show BSIT subject lists
@app.route('/BSIT_Subject_List', methods = ["POST", "GET"])
def BSIT_Subject_List():
    bsit_subjects_list=''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_data = cursor.execute("SELECT * FROM subject WHERE program = 'IT' AND course_type = 'Subject' ORDER BY subjectname ASC")

    if bsit_data > 0:
        bsit_subjects_list = cursor.fetchall()
    
    if request.method == 'POST' and 'search_subject' in request.form:
        search_subject = request.form['search_subject']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        bsit_data = cursor.execute("SELECT * FROM subject WHERE program = 'IT' AND subjectcode = %s AND course_type = 'Subject' ORDER BY subjectname ASC",[search_subject])
        
        if bsit_data > 0:
            bsit_subjects_list = cursor.fetchall()
            
        else:
            flash('NO DATA FOUND!')
        
    return render_template('bsit_subject_list.html', bsit_subjects_list = bsit_subjects_list)

# ADD BSIT Subject
@app.route("/BSIT_Add_Subject", methods = ["POST","GET"])
def BSIT_Add_Subject():
    
    if request.method == 'POST' and 'subjectcode' in request.form and 'subjectname' in request.form and 'section' in request.form:
        # Create variables for easy access
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'IT'
        course_type = 'Subject'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("New Added Subject & Section are Already Existed in BSIT Subject List!")
            return render_template('error.html')

        else:
            
            # Insert new data into itmeeting table
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO subject VALUES (%s, %s, %s, %s, %s)',(subjectcode, subjectname, section, program, course_type,))
            mysql.connection.commit()
            cursor.close()
            msg = 'New record created successfully'
            return jsonify(msg)

# Edit BSIT subject 
@app.route("/BSIT_Edit_Subject", methods = ["POST","GET"])
def BSIT_Edit_Subject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        string = request.form['string']
        subjectcode = request.form['subjectcode']
        subjectname = request.form['subjectname']
        section = request.form['section']
        program = 'IT'
        course_type = 'Subject'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM subject WHERE subjectcode = %s AND section = %s', (subjectcode, section,))

        subject_data = cursor.fetchone()
        
        if subject_data:

            subjectcode = subject_data['subjectcode']
            section = subject_data['section']
            flash("Your's Edited Subject & Section are Already Existed. Please type a different!")
            return render_template('error.html')

        else:
               
            cur.execute("UPDATE subject SET subjectcode = %s, subjectname = %s, section = %s, program = %s, course_type = %s  WHERE subjectcode = %s ", [subjectcode, subjectname, section, program, course_type, string])
            mysql.connection.commit()       
            cur.close()
            msg = 'Record successfully Updated'
            
            return jsonify(msg)

#Delete BSIT Project & Subject
@app.route("/BSIT_Delete_Subject", methods = ["POST","GET"])
def BSIT_Delete_Subject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM subject WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM offered_subject WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM defult_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM modify_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM codeshare WHERE subjectcode = %s',[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg) 

# ------------------------------------------------------------------------------------------------------------------------------
#                                                      Meeting                                                         
# ------------------------------------------------------------------------------------------------------------------------------

# >> Computer Science Meeting <<

#Show BSCS meeting data table
@app.route('/BSCS_Meeting', methods = ["POST", "GET"])
def BSCS_Meeting():
    
    bscs_data_details = ''
    meeting_details = ''
    print_meeting = ''

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_data = cursor.execute("SELECT * FROM meeting WHERE program = 'CS'")
    
    if bscs_data > 0:
        bscs_data_details = cursor.fetchall()

    if request.method == 'POST' and 'meeting_details' in request.form:
        meeting_details = request.form.getlist('meeting_details')
        print(meeting_details)
        session['meeting_details'] = meeting_details
    
    if meeting_details:
        mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mycursor.execute("SELECT subject.course_type, COUNT(offered_subject.subjectcode) FROM offered_subject LEFT JOIN subject ON offered_subject.subjectcode = subject.subjectcode WHERE offered_subject.program = 'CS' AND offered_subject.semester = %s GROUP BY course_type;",[meeting_details])
        subject_count = mycursor.fetchall()
        
        subject_counted = [str(i) for i in subject_count]
        subj_counted_res = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), subject_counted))
        
        subj_counted_res_cs_p = subj_counted_res[0]
        subj_counted_res_cs_s = subj_counted_res[1]
        total_cs = int(subj_counted_res_cs_p) + int(subj_counted_res_cs_s)
        
        session['subj_counted_res_cs_p'] = subj_counted_res_cs_p
        session['subj_counted_res_cs_s'] = subj_counted_res_cs_s
        session['total_cs'] = total_cs
        
        print(subj_counted_res_cs_p, subj_counted_res_cs_s)
        
        return redirect(url_for('BSCS_Meeting_Detail')) 
    
    if request.method == 'POST' and 'print_meeting' in request.form:
       print_meeting = request.form.getlist('print_meeting')
       print("Print Meeting",print_meeting)
       session['print_meeting'] = print_meeting
    
    if print_meeting:
        return redirect(url_for('CoverPage'))

    return render_template('bscs_meeting.html', bscs_data_details = bscs_data_details, meeting_details = meeting_details)
# ------------------------------------------------------------------------------------------------------------------------------

# >> Cover Page <<

@app.route('/CoverPage', methods = ["POST", "GET"])
def CoverPage():
    meeting_lists = ''
    meeting_committee_lists = ''    
    print_meeting = session.get('print_meeting')

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    meeting_list = cursor.execute("SELECT * FROM meeting WHERE program = 'CS' AND semester = %s",[print_meeting,])
    if meeting_list > 0:
        meeting_lists = cursor.fetchall()
        
    meeting_committee = cursor.execute("SELECT * FROM meeting_committee")
    if meeting_committee > 0:
        meeting_committee_lists = cursor.fetchall()
        
    if request.method == 'POST':
        if request.form['download'] == 'download':
            return redirect(url_for('BSCS_Meeting'))
        
    return render_template('bscs_cover_page.html', meeting_lists = meeting_lists, meeting_committee_lists = meeting_committee_lists)
# ------------------------------------------------------------------------------------------------------------------------------


#Create New BSCS Meeting 
@app.route("/BSCS_Create_Meeting", methods = ["POST", "GET"])
def BSCS_Create_Meeting():
    MeetingDate = ''
    bscs_committe = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_committes = cursor.execute("SELECT * FROM meeting_committee WHERE program = 'CS'")
    if bscs_committes > 0:
        bscs_committe = cursor.fetchall()
        
    MeetingDates = cursor.execute("SELECT * FROM meeting WHERE program = 'CS' ORDER BY insertDate DESC LIMIT 1")
    if MeetingDates > 0:
        MeetingDate = cursor.fetchall()

    if request.method == 'POST' and 'meetingnumber' in request.form and 'semester' in request.form and 'date' in request.form and 'time' in request.form and 'venue' in request.form:
        # Create variables for easy access
        meetingnumber = request.form['meetingnumber']
        semester = request.form['semester']
        date = request.form['date']
        time = request.form['time']
        program = 'CS'
        venue = request.form['venue']
        insertDate = datetime.now()
        
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO meeting VALUES (%s, %s, %s, %s, %s, %s, %s)',(meetingnumber, semester, date, time, program, venue, insertDate))
            mysql.connection.commit()
            return redirect(url_for('BSCS_Meeting'))
       
        except:
            flash("This Meeting Number is already in use!")
            return redirect(url_for('BSCS_Create_Meeting'))

    return render_template('bscs_create_meeting.html', bscs_committe = bscs_committe, MeetingDate = MeetingDate)

#Edit BSCS meeting data
@app.route("/BSCS_Edit_Meeting", methods = ["POST","GET"])
def BSCS_Edit_Meeting():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        meetingnumber = request.form['meetingnumber']
        semester = request.form['semester']
        date = request.form['date']
        time = request.form['time']
        program = 'CS'
        venue = request.form['venue']
        
        cur.execute("UPDATE meeting SET meetingnumber = %s, semester = %s, date = %s, time = %s, program = %s, venue = %s WHERE meetingnumber = %s ", [meetingnumber, semester, date, time, program, venue, string])
        mysql.connection.commit()
        cur.close()
        msg = 'Record successfully Updated'
        
        return jsonify(msg)

#Delete BSCS meeting data
@app.route("/BSCS_Delete_Meeting", methods = ["POST","GET"])
def BSCS_Delete_Meeting():
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM meeting WHERE meetingnumber = %s',[getid])
        mysql.connection.commit()
        cur.close()
        msg = 'Record deleted successfully'
        return jsonify(msg) 

# ------------------------------------------------------------------------------------------------------------------------------

# >> Information Technology Meeting<<

#Show BSIT meeting data
@app.route('/BSIT_Meeting', methods = ["POST","GET"])
def BSIT_Meeting():
    
    bsit_data_details = ''
    it_meeting_details = ''

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_data = cursor.execute("SELECT * FROM meeting WHERE program = 'IT'")
    
    if bsit_data > 0:
        bsit_data_details = cursor.fetchall()

    if request.method == 'POST' and 'meeting_details' in request.form:
        it_meeting_details = request.form.getlist('meeting_details')
        print(it_meeting_details)
        session['it_meeting_details'] = it_meeting_details
    
    if it_meeting_details:
        mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mycursor.execute("SELECT subject.course_type, COUNT(offered_subject.subjectcode) FROM offered_subject LEFT JOIN subject ON offered_subject.subjectcode = subject.subjectcode WHERE offered_subject.program = 'IT' AND offered_subject.semester = %s GROUP BY course_type;",[it_meeting_details])
        subject_count = mycursor.fetchall()
        
        subject_counted = [str(i) for i in subject_count]
        subj_counted_res = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), subject_counted))
        
        subj_counted_res_it_p = subj_counted_res[0]
        subj_counted_res_it_s = subj_counted_res[1]
        total_it = int(subj_counted_res_it_p) + int(subj_counted_res_it_s)
        
        session['subj_counted_res_it_p'] = subj_counted_res_it_p
        session['subj_counted_res_it_s'] = subj_counted_res_it_s
        session['total_it'] = total_it
        
        print(subj_counted_res_it_p, subj_counted_res_it_s)
        
        return redirect(url_for('BSIT_Meeting_Detail')) 

    return render_template('bsit_meeting.html', bsit_data_details = bsit_data_details, it_meeting_details = it_meeting_details )

#Create New BSIT meeting
@app.route("/BSIT_Create_Meeting", methods = ["POST", "GET"])
def BSIT_Create_Meeting():

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_committe = cursor.execute("SELECT * FROM committee WHERE program = 'IT'")

    if bsit_committe > 0:
        bsit_committe = cursor.fetchall()

    if request.method == 'POST' and 'meetingnumber' in request.form and 'semester' in request.form and 'date' in request.form and 'time' in request.form and 'venue' in request.form:

        meetingnumber = request.form['meetingnumber']
        semester = request.form['semester']
        date = request.form['date']
        time = request.form['time']
        program = 'IT'
        venue = request.form['venue']
        
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO meeting VALUES (%s, %s, %s, %s, %s, %s)',(meetingnumber, semester, date, time, program, venue,))
            mysql.connection.commit()
            return redirect(url_for('BSIT_Meeting'))
       
        except:
            flash("This Meeting Number is already in use!")
            return redirect(url_for('BSIT_Create_Meeting'))

    return render_template('bsit_create_meeting.html', bsit_committe = bsit_committe)

#Edit BSIT meeting data
@app.route("/BSIT_Edit_Meeting", methods = ["POST","GET"])
def BSIT_Edit_Meeting():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        meetingnumber = request.form['meetingnumber']
        semester = request.form['semester']
        date = request.form['date']
        time = request.form['time']
        program = 'IT'
        venue = request.form['venue']
        
        cur.execute("UPDATE meeting SET meetingnumber = %s, semester = %s, date = %s, time = %s, program = %s, venue = %s WHERE meetingnumber = %s ", [meetingnumber, semester, date, time, program, venue, string])
        mysql.connection.commit()
        cur.close()
        msg = 'Record successfully Updated'
        
        return jsonify(msg)

#Delete BSIT meeting data
@app.route("/BSIT_Delete_Meeting", methods = ["POST","GET"])
def BSIT_Delete_Meeting():
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM meeting WHERE meetingnumber = %s',[getid])
        mysql.connection.commit()
        cur.close()
        msg = 'Record deleted successfully'
        return jsonify(msg) 

# ------------------------------------------------------------------------------------------------------------------------------
#                                                      Meeting Details                                                         
# ------------------------------------------------------------------------------------------------------------------------------

#        >> Computer Science <<    

@app.route('/BSCS_Meeting_Detail', methods = ["POST","GET"])
def BSCS_Meeting_Detail():
    
    meeting_result= ''
    meeting_sem_result = ''
    approved_cs_res = ''
    changed_cs_res = ''
    grade_result = ''
    
    subj_counted_res_cs_p = session.get('subj_counted_res_cs_p')
    subj_counted_res_cs_s = session.get('subj_counted_res_cs_s')
    total_cs = session.get('total_cs')
    meeting_details = session.get('meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    #Show if not grade exists
    check_grade = cursor.execute("SELECT offered_subject.subjectcode, subject.subjectname, subject.section, offered_subject.approved, offered_subject.changed FROM offered_subject LEFT JOIN defult_grade ON defult_grade.subjectcode = offered_subject.subjectcode JOIN subject ON offered_subject.subjectcode = subject.subjectcode WHERE defult_grade.subjectcode is NULL AND offered_subject.program = 'CS' AND offered_subject.semester = %s",[meeting_details])
    if check_grade > 0:
        grade_result = cursor.fetchall()
        
    #Show if grade exists
    meeting_offered_subject = cursor.execute("SELECT * FROM offered_subject JOIN subject ON subject.subjectcode = offered_subject.subjectcode JOIN defult_grade ON defult_grade.subjectcode = offered_subject.subjectcode WHERE offered_subject.program = 'CS' AND offered_subject.semester = %s ORDER BY subject.subjectname ASC",[meeting_details])
    if meeting_offered_subject > 0:
        meeting_result = cursor.fetchall()
    
    meeting_sem = cursor.execute("SELECT DISTINCT semester FROM offered_subject WHERE semester = %s",[meeting_details])
    if meeting_sem > 0:
        meeting_sem_result = cursor.fetchall()
    
    #Count Approved subject
    cursor.execute("SELECT COUNT(approved) FROM offered_subject WHERE APPROVED = 1 AND program = 'CS'")
    approved = cursor.fetchall()
    
    approved_count = [str(i) for i in approved]
    approved_cs = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), approved_count))
    approved_cs_res = str(approved_cs[0])
    print(str(approved_cs_res))
    session['approved_cs_res'] = approved_cs_res
    
    #Count Changed Subject
    cursor.execute("SELECT COUNT(changed) FROM offered_subject WHERE changed = 1 AND program = 'CS'")
    changed = cursor.fetchall()
    
    changed_count = [str(i) for i in changed]
    changed_cs = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), changed_count))
    changed_cs_res = str(changed_cs[0])
    print(str(changed_cs_res))
    session['changed_cs_res'] = changed_cs_res
    
    if request.method == 'POST' and 'cs_graderange' in request.form:
        cs_graderange = request.form.getlist('cs_graderange')
        print(cs_graderange)
        session['cs_graderange'] = cs_graderange
        
        approved = cursor.execute("SELECT approved FROM offered_subject WHERE subjectcode = %s", [cs_graderange])
        if approved > 0:
            check_approved = cursor.fetchone() 
        
            if check_approved['approved'] ==  1:
                return redirect(url_for('BSCS_Grade_Approved'))

            else:
                return redirect(url_for('BSCS_Show_Grade'))
    
    return render_template('bscs_meeting_detail.html', grade_result=grade_result, subj_counted_res_cs_p = subj_counted_res_cs_p, subj_counted_res_cs_s = subj_counted_res_cs_s, total_cs = total_cs, meeting_result = meeting_result, meeting_sem_result = meeting_sem_result, approved_cs_res = approved_cs_res, changed_cs_res=changed_cs_res)

# ------------------------------------------------------------------------------------------------------------------------------

#        >> Meeting Details For Information Technology <<    

@app.route('/BSIT_Meeting_Detail', methods = ["POST","GET"])
def BSIT_Meeting_Detail():
    meeting_result= ''
    meeting_sem_result = ''
    approved_it_res = ''
    changed_it_res = ''
    grade_result = ''
    
    subj_counted_res_it_p = session.get('subj_counted_res_it_p')
    subj_counted_res_it_s = session.get('subj_counted_res_it_s')
    total_it = session.get('total_it')
    it_meeting_details = session.get('it_meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
     #Show if not grade exists
    check_grade = cursor.execute("SELECT offered_subject.subjectcode, subject.subjectname, subject.section, offered_subject.approved, offered_subject.changed FROM offered_subject LEFT JOIN defult_grade ON defult_grade.subjectcode = offered_subject.subjectcode JOIN subject ON offered_subject.subjectcode = subject.subjectcode WHERE defult_grade.subjectcode is NULL AND offered_subject.program = 'IT' AND offered_subject.semester = %s",[it_meeting_details])
    if check_grade > 0:
        grade_result = cursor.fetchall()
        
    #Show if grade exists
    meeting_offered_subject = cursor.execute("SELECT * FROM offered_subject JOIN subject ON subject.subjectcode = offered_subject.subjectcode JOIN defult_grade ON defult_grade.subjectcode = offered_subject.subjectcode WHERE offered_subject.program = 'IT' AND offered_subject.semester = %s ORDER BY subject.subjectname ASC",[it_meeting_details])
    if meeting_offered_subject > 0:
        meeting_result = cursor.fetchall()
    
    meeting_sem = cursor.execute("SELECT DISTINCT semester FROM offered_subject WHERE semester = %s",[it_meeting_details])
    if meeting_sem > 0:
        meeting_sem_result = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(changed) FROM offered_subject WHERE changed = 1 AND program = 'IT'")
    changed = cursor.fetchall()
    
    changed_count = [str(i) for i in changed]
    changed_it = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), changed_count))
    changed_it_res = str(changed_it[0])
    print(str(changed_it_res))
    session['changed_it_res'] = changed_it_res
    
    cursor.execute("SELECT COUNT(approved) FROM offered_subject WHERE APPROVED = 1 AND program = 'IT'")
    approved = cursor.fetchall()
    
    approved_count = [str(i) for i in approved]
    approved_it = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), approved_count))
    approved_it_res = str(approved_it[0])
    print(str(approved_it_res))
    
    session['approved_it_res'] = approved_it_res
    
    if request.method == 'POST' and 'it_graderange' in request.form:
        it_graderange = request.form.getlist('it_graderange')
        print(it_graderange)
        session['it_graderange'] = it_graderange
        
        approved = cursor.execute("SELECT approved FROM offered_subject WHERE subjectcode = %s", [it_graderange])
        if approved > 0:
            check_approved = cursor.fetchone() 
        
            if check_approved['approved'] ==  1:
                return redirect(url_for('BSIT_Grade_Approved'))

            else:
                return redirect(url_for('BSIT_Show_Grade'))
    
    return render_template('bsit_meeting_detail.html', grade_result = grade_result, changed_it_res = changed_it_res, subj_counted_res_it_p = subj_counted_res_it_p, subj_counted_res_it_s = subj_counted_res_it_s, total_it = total_it, meeting_result = meeting_result, meeting_sem_result = meeting_sem_result, approved_it_res = approved_it_res)

# ------------------------------------------------------------------------------------------------------------------------------
#                                                      Grading                                                         
# ------------------------------------------------------------------------------------------------------------------------------

#        >> Computer Science Grade Range<<    

@app.route('/BSCS_Show_Grade', methods = ["POST","GET"])
def BSCS_Show_Grade():
    
    CodeshareResult = ''
    codeshare_output = ''
    modify_grade = ''
    result = ''
    defult_total_students = ''
    modify_total_students = ''
    cs_codeshare = ''
    cs_l = []
    cs_code = ''
    
    cs_graderange = session.get('cs_graderange')
    meeting_details = session.get('meeting_details')
            
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[cs_graderange])
    if meeting_offered_subject > 0:
        CodeshareResult = cursor.fetchall()
        
        #Total Number Of Students
        cursor.execute("SELECT SUM(COALESCE(A_students,0)+COALESCE(A_minus_students,0)+COALESCE(B_plus_students,0)+COALESCE(B_students,0)+COALESCE(B_minus_students,0)+COALESCE(C_plus_students,0)+COALESCE(C_students,0)+COALESCE(C_minus_students,0)+COALESCE(D_students,0)+COALESCE(F_students,0)+COALESCE(I_students,0)+COALESCE(W_students,0)) AS defult_total_student FROM defult_grade WHERE subjectcode = %s",[cs_graderange])
        defult_total_student = cursor.fetchone()
        if defult_total_student['defult_total_student'] == defult_total_student['defult_total_student']:
            defult_total_students = int(defult_total_student['defult_total_student'])
        
        cursor.execute("SELECT SUM(COALESCE(A_students,0)+COALESCE(A_minus_students,0)+COALESCE(B_plus_students,0)+COALESCE(B_students,0)+COALESCE(B_minus_students,0)+COALESCE(C_plus_students,0)+COALESCE(C_students,0)+COALESCE(C_minus_students,0)+COALESCE(D_students,0)+COALESCE(F_students,0)+COALESCE(I_students,0)+COALESCE(W_students,0)) AS total FROM modify_grade WHERE subjectcode = %s",[cs_graderange])
        total_student = cursor.fetchone()
        if total_student['total'] == total_student['total']:
            modify_total_students = int(total_student['total'])

    else:
        return redirect(url_for('BSCS_ErrorGrade'))
    
    modify_grade = cursor.execute("SELECT * FROM modify_grade INNER JOIN subject ON subject.subjectcode = modify_grade.subjectcode WHERE modify_grade.subjectcode = %s",[cs_graderange])
    if modify_grade > 0:
        modify_grade = cursor.fetchall()
    else:
        return redirect(url_for('BSCS_ErrorGrade'))
    
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[cs_graderange, meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
    
    #Take Codeshare Subject
    codeshare = cursor.execute("SELECT codeshare_subject FROM codeshare WHERE subjectcode = %s",[cs_graderange])
    if codeshare > 0:
        codeshare = cursor.fetchall()
        for output in codeshare:
            if output['codeshare_subject'] == output['codeshare_subject']:
                cs_codeshare = output['codeshare_subject']
                cs_l.append(cs_codeshare)
                print("All codeshare: ", cs_l)
        
    if request.method == 'POST':
        if request.form['btn_approved'] == 'btn_approved': 
            
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE offered_subject SET approved = True WHERE subjectcode = %s",[cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[cs_graderange])
            mysql.connection.commit()
            
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE offered_subject SET approved = True WHERE subjectcode = %s",[cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
                print('Done')
            return redirect(url_for('BSCS_Grade_Approved'))
            
    return render_template('bscs_show_grade.html', defult_total_students=defult_total_students, modify_total_students=modify_total_students, CodeshareResult=CodeshareResult, result=result, modify_grade=modify_grade, codeshare_output=codeshare_output)

@app.route('/BSCS_ErrorGrade', methods = ["POST","GET"])
def BSCS_ErrorGrade():
    
    A_max = '100'
    subject_name = ''
    
    cs_graderange = session.get('cs_graderange')
    meeting_details = session.get('meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[cs_graderange])
    subject_name = cursor.fetchall()
    
    if 'set_grade' in request.form:
        cursor.execute("INSERT INTO defult_grade (semester, subjectcode, A_max) VALUES  (%s, %s, %s)", [meeting_details, cs_graderange, A_max])
        cursor.execute("INSERT INTO modify_grade (semester, subjectcode, A_min, A_max, A_students, A_minus_min, A_minus_max, A_minus_students, B_plus_min, B_plus_max, B_plus_students, B_min, B_max, B_students, B_minus_min, B_minus_max, B_minus_students, C_plus_min, C_plus_max, C_plus_students, C_min, C_max, C_students, C_minus_min, C_minus_max, C_minus_students, D_min, D_max, D_students, F_min, F_max, F_students, I_min, I_max, I_students, W_min, W_max, W_students) VALUES  (%s, %s, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')", [meeting_details, cs_graderange])
        mysql.connection.commit()
        return redirect(url_for('BSCS_SetGrade'))
        
    return render_template('bscs_error_grade.html',subject_name=subject_name)

@app.route('/BSCS_SetGrade', methods = ["POST","GET"])
def BSCS_SetGrade():
    
    A_minus_max = ''
    B_plus_max = ''
    B_max = ''
    B_minus_max = ''
    C_plus_max = ''
    C_max = ''
    C_minus_max = ''
    D_max = ''
    D_min = ''
    F_max = ''
    subject_name_result = ''
    F_min = '0'
    I_min = '-'
    I_max = '-'
    W_min = '-'
    W_max = '-'
    show_gradeRange = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cs_graderange = session.get('cs_graderange')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[cs_graderange])
    if meeting_offered_subject > 0:
        show_gradeRange = cursor.fetchall()
    
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[cs_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
    
    if request.method == 'POST':
        A_min = request.form.get('A_min', type=int)
        A_minus_min = request.form.get('A_minus_min', type=int)
        B_plus_min = request.form.get('B_plus_min', type=int)
        B_min = request.form.get('B_min', type=int)
        B_minus_min = request.form.get('B_minus_min', type=int)
        C_plus_min = request.form.get('C_plus_min', type=int)
        C_min = request.form.get('C_min', type=int)
        C_minus_min = request.form.get('C_minus_min', type=int)
        D_min = request.form.get('D_min', type=int)

        if A_min:
            A_minus_max = A_min - 1
            cursor.execute("UPDATE defult_grade SET A_min = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_minus_max, cs_graderange])
            mysql.connection.commit()
            
        if A_minus_min:
            B_plus_max = A_minus_min - 1
            cursor.execute("UPDATE defult_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, cs_graderange])
            mysql.connection.commit()
            
        if B_plus_min:
            B_max = B_plus_min - 1
            cursor.execute("UPDATE defult_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, cs_graderange])
            mysql.connection.commit()
            
        if B_min:
            B_minus_max = B_min - 1
            cursor.execute("UPDATE defult_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, cs_graderange])
            mysql.connection.commit()
            
        if B_minus_min:
            C_plus_max = B_minus_min - 1
            cursor.execute("UPDATE defult_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, cs_graderange])
            mysql.connection.commit()
            
        if C_plus_min:
            C_max = C_plus_min - 1
            cursor.execute("UPDATE defult_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, cs_graderange])
            mysql.connection.commit()
            
        if C_min:
            C_minus_max = C_min - 1
            cursor.execute("UPDATE defult_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, cs_graderange])
            mysql.connection.commit()
            
        if C_minus_min:
            D_max = C_minus_min - 1
            cursor.execute("UPDATE defult_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, cs_graderange])
            mysql.connection.commit()
            
        if D_min:
            F_max = D_min - 1
            cursor.execute("UPDATE defult_grade SET D_min = %s, F_min = %s, F_max = %s, I_min = %s, I_max = %s, W_min = %s, W_max = %s WHERE subjectcode = %s",[D_min, F_min, F_max, I_min, I_max, W_min, W_max, cs_graderange])
            mysql.connection.commit()
        
        cursor.execute("UPDATE defult_grade SET A_students = '-' WHERE A_students IS NULL")
        cursor.execute("UPDATE defult_grade SET A_minus_students = '-' WHERE A_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_plus_students = '-' WHERE B_plus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_students = '-' WHERE B_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_minus_students = '-' WHERE B_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_plus_students = '-' WHERE C_plus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_students = '-' WHERE C_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_minus_students = '-' WHERE C_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET D_students = '-' WHERE D_students IS NULL")
        cursor.execute("UPDATE defult_grade SET F_students = '-' WHERE F_students IS NULL")
        cursor.execute("UPDATE defult_grade SET I_students = '-' WHERE I_students IS NULL")
        cursor.execute("UPDATE defult_grade SET W_students = '-' WHERE W_students IS NULL")
        
        cursor.execute("UPDATE defult_grade SET A_min = '-' WHERE A_min IS NULL")
        cursor.execute("UPDATE defult_grade SET A_minus_min = '-' WHERE A_minus_min IS NULL")
        cursor.execute("UPDATE defult_grade SET A_minus_max = '-' WHERE A_minus_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET B_plus_min = '-' WHERE B_plus_min IS NULL")
        cursor.execute("UPDATE defult_grade SET B_plus_max = '-' WHERE B_plus_max IS NULL")
        cursor.execute("UPDATE defult_grade SET B_min = '-' WHERE B_min IS NULL")
        cursor.execute("UPDATE defult_grade SET B_max = '-' WHERE B_max IS NULL")
        cursor.execute("UPDATE defult_grade SET B_minus_min = '-' WHERE B_minus_min IS NULL")
        cursor.execute("UPDATE defult_grade SET B_minus_max = '-' WHERE B_minus_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET C_plus_min = '-' WHERE C_plus_min IS NULL")
        cursor.execute("UPDATE defult_grade SET C_plus_max = '-' WHERE C_plus_max IS NULL")
        cursor.execute("UPDATE defult_grade SET C_min = '-' WHERE C_min IS NULL")
        cursor.execute("UPDATE defult_grade SET C_max = '-' WHERE C_max IS NULL")
        cursor.execute("UPDATE defult_grade SET C_minus_min = '-' WHERE C_minus_min IS NULL")
        cursor.execute("UPDATE defult_grade SET C_minus_max = '-' WHERE C_minus_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET D_min = '-' WHERE D_min IS NULL")
        cursor.execute("UPDATE defult_grade SET D_max = '-' WHERE D_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET F_min = '-' WHERE F_min IS NULL")
        cursor.execute("UPDATE defult_grade SET F_max = '-' WHERE F_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET I_min = '-' WHERE I_min IS NULL")
        cursor.execute("UPDATE defult_grade SET I_max = '-' WHERE I_max IS NULL")
        
        cursor.execute("UPDATE defult_grade SET W_min = '-' WHERE W_min IS NULL")
        cursor.execute("UPDATE defult_grade SET W_max = '-' WHERE W_max IS NULL")
        
    if request.method == "POST":
        A_students = request.form.get('A_students')
        A_minus_students = request.form.get('A_minus_students')
        B_plus_students = request.form.get('B_plus_students')
        B_students = request.form.get('B_students')
        B_minus_students = request.form.get('B_minus_students')
        C_plus_students = request.form.get('C_plus_students')
        C_students = request.form.get('C_students')
        C_minus_students = request.form.get('C_minus_students')
        D_students = request.form.get('D_students')
        F_students = request.form.get('F_students')
        I_students = request.form.get('I_students')
        W_students = request.form.get('W_students')
        
        if A_students:
            if request.form.get('A_students') == '0':
                print("A IS 0")
                A_students = '-'
                cursor.execute("UPDATE defult_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_graderange])
                mysql.connection.commit()
            
        if A_minus_students:
            if request.form.get('A_minus_students') == '0':
                A_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_graderange])
                mysql.connection.commit()
            
        if B_plus_students:
            if request.form.get('B_plus_students') == '0':
                B_plus_students = '-'
                cursor.execute("UPDATE defult_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_graderange])
                mysql.connection.commit()   
            
        if B_students:
            if request.form.get('B_students') == '0':
                B_students = '-'
                cursor.execute("UPDATE defult_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_graderange])
                mysql.connection.commit()
            
        if B_minus_students:
            if request.form.get('B_minus_students') == '0':
                B_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_graderange])
                mysql.connection.commit()
            
        if C_plus_students:
            if request.form.get('C_plus_students') == '0':
                C_plus_students = '-'
                cursor.execute("UPDATE defult_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_graderange])
                mysql.connection.commit()
            else:
                cursor.execute("UPDATE defult_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_graderange])
                mysql.connection.commit()
            
        if C_students:
            if request.form.get('C_students') == '0':
                C_students = '-'
                cursor.execute("UPDATE defult_grade SET C_students = %s WHERE subjectcode = %s", [C_students, cs_graderange])
                mysql.connection.commit()
            
        if C_minus_students:
            if request.form.get('C_minus_students') == '0':
                C_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_graderange])
                mysql.connection.commit()
            
        if D_students:
            if request.form.get('D_students') == '0':
                D_students = '-'
                cursor.execute("UPDATE defult_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_graderange])
                mysql.connection.commit()
        
        if F_students:
            if request.form.get('F_students') == '0':
                F_students = '-'
                cursor.execute("UPDATE defult_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_graderange])
                mysql.connection.commit()
        
        if I_students:
            if request.form.get('I_students') == '0':
                I_students = '-'
                cursor.execute("UPDATE defult_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_graderange])
                mysql.connection.commit()
        
        if W_students:
            if request.form.get('W_students') == '0':
                W_students = '-'
                cursor.execute("UPDATE defult_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_graderange])
                mysql.connection.commit()
            
    return render_template("bscs_setgrade.html", show_gradeRange=show_gradeRange, subject_name_result=subject_name_result, A_minus_max=A_minus_max, B_plus_max=B_plus_max, B_max=B_max, B_minus_max=B_minus_max, C_plus_max=C_plus_max, C_max=C_max, C_minus_max=C_minus_max, D_max=D_max, F_max=F_max)

@app.route('/BSCS_Grade_Approved', methods = ["POST","GET"])
def BSCS_Grade_Approved():
    
    defult_grade_result = ''
    modify_grade_result = ''
    subject_name_result = ''
    result = ''
    meeting_result = ''
    defult_total_students = ''
    modify_total_students = ''
    modified = ''
    
    cs_graderange = session.get('cs_graderange')
    meeting_details = session.get('meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    cursor.execute("SELECT SUM(A_students)+SUM(A_minus_students)+SUM(B_plus_students)+SUM(B_students)+SUM(B_minus_students)+SUM(C_plus_students)+SUM(C_students)+SUM(C_minus_students)+SUM(D_students)+SUM(F_students)+SUM(I_students)+SUM(W_students) AS defult_total_student FROM defult_grade WHERE subjectcode = %s",[cs_graderange])
    defult_total_student = cursor.fetchone()
    if defult_total_student['defult_total_student'] == defult_total_student['defult_total_student']:
        defult_total_students = int(defult_total_student['defult_total_student'])
    
    cursor.execute("SELECT SUM(A_students)+SUM(A_minus_students)+SUM(B_plus_students)+SUM(B_students)+SUM(B_minus_students)+SUM(C_plus_students)+SUM(C_students)+SUM(C_minus_students)+SUM(D_students)+SUM(F_students)+SUM(I_students)+SUM(W_students) AS total FROM modify_grade WHERE subjectcode = %s",[cs_graderange])
    total_student = cursor.fetchone()
    if total_student['total'] == total_student['total']:
        modify_total_students = int(total_student['total'])
            
    modify = cursor.execute("SELECT * FROM modify_grade INNER JOIN subject ON subject.subjectcode = modify_grade.subjectcode WHERE modify_grade.subjectcode = %s",[cs_graderange])
    if modify > 0:
        modify_grade_result = cursor.fetchall()
        
    defult = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[cs_graderange])
    if defult > 0:
        defult_grade_result = cursor.fetchall()
    
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[cs_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
    
    meeting_data = cursor.execute("SELECT * FROM meeting WHERE semester = %s AND program = 'CS'",[meeting_details])
    if meeting_data > 0:
        meeting_result = cursor.fetchall()
    
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[cs_graderange, meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
    
    check_data = cursor.execute("SELECT modified FROM offered_subject WHERE subjectcode = %s",[cs_graderange])
    if check_data > 0:
        checked = cursor.fetchone()
    
        if checked['modified'] == True:
            modified = 'Modified'
        
        else:
            modified = 'Approved' 
        
    if request.method == 'POST':
        if request.form['download'] == 'download':
            return redirect(url_for('BSCS_Meeting_Detail'))
        
    return render_template('bscs_approved_grade.html', modified = modified, meeting_result=meeting_result, modify_total_students=modify_total_students, defult_total_students=defult_total_students, modify_grade_result = modify_grade_result, meeting_details = meeting_details, subject_name_result = subject_name_result, result=result, defult_grade_result = defult_grade_result)

@app.route("/BSCS_Grade_Change", methods = ["POST","GET"])
def BSCS_Grade_Change():
    
    A_max = '100'
    A_minus_max = ''
    B_plus_max = ''
    B_max = ''
    B_minus_max = ''
    C_plus_max = ''
    C_max = ''
    C_minus_max = ''
    D_max = ''
    D_min = ''
    F_max = ''
    F_min = '0'
    
    show_gradeRange = ''
    subject_name_result = ''
    result = ''
    cs_codeshare = ''
    cs_l = []
    cs_code = ''
    
    cs_graderange = session.get('cs_graderange')
    meeting_details = session.get('meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[cs_graderange])
    if meeting_offered_subject > 0:
        show_gradeRange = cursor.fetchall()
    
    #Take Codeshare Subject
    codeshare = cursor.execute("SELECT codeshare_subject FROM codeshare WHERE subjectcode = %s",[cs_graderange])
    if codeshare > 0:
        codeshare = cursor.fetchall()
        for output in codeshare:
            if output['codeshare_subject'] == output['codeshare_subject']:
                cs_codeshare = output['codeshare_subject']
                cs_l.append(cs_codeshare)
                print("All codeshare: ", cs_l)
    
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[cs_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
    
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[cs_graderange, meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
        
    if request.method == 'POST':
        
        A_min = request.form.get('A_min', type=int) 
        A_minus_min = request.form.get('A_minus_min', type=int)
        B_plus_min = request.form.get('B_plus_min', type=int)
        B_min = request.form.get('B_min', type=int)
        B_minus_min = request.form.get('B_minus_min', type=int)
        C_plus_min = request.form.get('C_plus_min', type=int)
        C_min = request.form.get('C_min', type=int)
        C_minus_min = request.form.get('C_minus_min', type=int)
        D_min = request.form.get('D_min', type=int)
        
        A_students = request.form.get('A_students')
        A_minus_students = request.form.get('A_minus_students')
        B_plus_students = request.form.get('B_plus_students')
        B_students = request.form.get('B_students')
        B_minus_students = request.form.get('B_minus_students')
        C_plus_students = request.form.get('C_plus_students')
        C_students = request.form.get('C_students')
        C_minus_students = request.form.get('C_minus_students')
        D_students = request.form.get('D_students')
        F_students = request.form.get('F_students')
        I_students = request.form.get('I_students')
        W_students = request.form.get('W_students')
        
        if A_min:
            A_minus_max = A_min - 1
            cursor.execute("UPDATE modify_grade SET A_min = %s, A_max = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_max, A_minus_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True  WHERE subjectcode = %s",[cs_graderange])
            mysql.connection.commit()
            #To change aslo for the Codeshare Grade
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET A_min = %s, A_max = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_max, A_minus_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if A_minus_min:
            B_plus_max = A_minus_min - 1
            cursor.execute("UPDATE modify_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True  WHERE subjectcode = %s",[cs_graderange])
            mysql.connection.commit()
            #To change aslo for the Codeshare Grade
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if B_plus_min:
            B_max = B_plus_min - 1
            cursor.execute("UPDATE modify_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if B_min:
            B_minus_max = B_min - 1
            cursor.execute("UPDATE modify_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if B_minus_min:
            C_plus_max = B_minus_min - 1
            cursor.execute("UPDATE modify_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if C_plus_min:
            C_max = C_plus_min - 1
            cursor.execute("UPDATE modify_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if C_min:
            C_minus_max = C_min - 1
            cursor.execute("UPDATE modify_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if C_minus_min:
            D_max = C_minus_min - 1
            cursor.execute("UPDATE modify_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
            
        if D_min:
            F_max = D_min - 1
            cursor.execute("UPDATE modify_grade SET D_min = %s, F_min = %s, F_max = %s WHERE subjectcode = %s",[D_min, F_min, F_max, cs_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
            mysql.connection.commit()
            for cs_code in range(len(cs_l)):
                cs_codeshare = cs_l[cs_code]
                cursor.execute("UPDATE modify_grade SET D_min = %s, F_min = %s, F_max = %s WHERE subjectcode = %s",[D_min, F_min, F_max, cs_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
        
        if A_students:
            if request.form.get('A_students') == '0':
                A_students = '-'
                cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_graderange])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_codeshare])
                    cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_graderange])
                cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, cs_codeshare])
                    cursor.execute("UPDATE offered_subject SET changed = True, modified = True WHERE subjectcode = %s",[cs_codeshare])
                    mysql.connection.commit()
            
        if A_minus_students:
            if request.form.get('A_minus_students') == '0':
                A_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, cs_codeshare])
                    mysql.connection.commit()
            
        if B_plus_students:
            if request.form.get('B_plus_students') == '0':
                B_plus_students = '-'
                cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_codeshare])
                    mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_codeshare])
                    mysql.connection.commit()
            
        if B_students:
            if request.form.get('B_students') == '0':
                B_students = '-'
                cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, cs_codeshare])
                    mysql.connection.commit()
            
        if B_minus_students:
            if request.form.get('B_minus_students') == '0':
                B_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, cs_codeshare])
                    mysql.connection.commit()
            
        if C_plus_students:
            if request.form.get('C_plus_students') == '0':
                C_plus_students = '-'
                cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, cs_codeshare])
                    mysql.connection.commit()
            
        if C_students:
            if request.form.get('C_students') == '0':
                C_students = '-'
                cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, cs_codeshare])
                    mysql.connection.commit()
            
        if C_minus_students:
            if request.form.get('C_minus_students') == '0':
                C_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_codeshare])
                    mysql.connection.commit()
                    
        if D_students:
            if request.form.get('D_students') == '0':
                D_students = '-'
                cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, cs_codeshare])
                    mysql.connection.commit()
        
        if F_students:
            if request.form.get('F_students') == '0':
                F_students = '-'
                cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, cs_codeshare])
                    mysql.connection.commit()
        
        if I_students:
            if request.form.get('I_students') == '0':
                I_students = '-'
                cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, cs_codeshare])
                    mysql.connection.commit()
        
        if W_students:
            if request.form.get('W_students') == '0':
                W_students = '-'
                cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(cs_l)):
                    cs_codeshare = cs_l[cs_code]
                    cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, cs_codeshare])
                    mysql.connection.commit()
            
    return render_template("bscs_grade_change.html", show_gradeRange = show_gradeRange, meeting_details = meeting_details, subject_name_result = subject_name_result, result = result, A_minus_max=A_minus_max, B_plus_max=B_plus_max, B_max=B_max, B_minus_max=B_minus_max, C_plus_max=C_plus_max, C_max=C_max, C_minus_max=C_minus_max, D_max=D_max, F_max=F_max)

# DELETE Grade Range
@app.route("/BSCS_Delete_GradeRange", methods = ["POST","GET"])
def BSCS_Delete_GradeRange():

    if request.method == 'POST':
        getid = request.form['string']

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('DELETE FROM defult_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM modify_grade WHERE subjectcode = %s',[getid])
        cur.execute("UPDATE offered_subject SET approved = False WHERE subjectcode = %s",[getid])
        cur.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[getid])
        mysql.connection.commit()
        cur.close()
        flash("DELETE SUCCESSFULLY")
        return redirect(url_for('BSCS_GradeRange_list'))
    
# ------------------------------------------------------------------------------------------------------------------------------

#        >> Information Technology Grade Range<<    

@app.route('/BSIT_Show_Grade', methods = ["POST","GET"])
def BSIT_Show_Grade():
    
    CodeshareResult = ''
    codeshare_output = ''
    modify_grade = ''
    result = ''
    defult_total_students = ''
    modify_total_students = ''
    it_codeshare = ''
    it_l = []
    it_code = ''
    
    it_graderange = session.get('it_graderange')
    it_meeting_details = session.get('it_meeting_details')
            
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[it_graderange])
    if meeting_offered_subject > 0:
        CodeshareResult = cursor.fetchall()
        
        #Total Number Of Students
        cursor.execute("SELECT SUM(COALESCE(A_students,0)+COALESCE(A_minus_students,0)+COALESCE(B_plus_students,0)+COALESCE(B_students,0)+COALESCE(B_minus_students,0)+COALESCE(C_plus_students,0)+COALESCE(C_students,0)+COALESCE(C_minus_students,0)+COALESCE(D_students,0)+COALESCE(F_students,0)+COALESCE(I_students,0)+COALESCE(W_students,0)) AS defult_total_student FROM defult_grade WHERE subjectcode = %s",[it_graderange])
        defult_total_student = cursor.fetchone()
        if defult_total_student['defult_total_student'] == defult_total_student['defult_total_student']:
            defult_total_students = int(defult_total_student['defult_total_student'])
        
        cursor.execute("SELECT SUM(COALESCE(A_students,0)+COALESCE(A_minus_students,0)+COALESCE(B_plus_students,0)+COALESCE(B_students,0)+COALESCE(B_minus_students,0)+COALESCE(C_plus_students,0)+COALESCE(C_students,0)+COALESCE(C_minus_students,0)+COALESCE(D_students,0)+COALESCE(F_students,0)+COALESCE(I_students,0)+COALESCE(W_students,0)) AS total FROM modify_grade WHERE subjectcode = %s",[it_graderange])
        total_student = cursor.fetchone()
        if total_student['total'] == total_student['total']:
            modify_total_students = int(total_student['total'])
            
    else:
        return redirect(url_for('BSIT_ErrorGrade'))
    
    modify_grade = cursor.execute("SELECT * FROM modify_grade INNER JOIN subject ON subject.subjectcode = modify_grade.subjectcode WHERE modify_grade.subjectcode = %s",[it_graderange])
    if modify_grade > 0:
        modify_grade = cursor.fetchall()
    else:
        return redirect(url_for('BSIT_ErrorGrade'))
    
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[it_graderange, it_meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
        
    #Take Codeshare Subject
    codeshare = cursor.execute("SELECT codeshare_subject FROM codeshare WHERE subjectcode = %s",[it_graderange])
    if codeshare > 0:
        codeshare = cursor.fetchall()
        for output in codeshare:
            if output['codeshare_subject'] == output['codeshare_subject']:
                it_codeshare = output['codeshare_subject']
                it_l.append(it_codeshare)
                print("All codeshare: ", it_l)
        
    if request.method == 'POST':
        if request.form['btn_approved'] == 'btn_approved': 
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE offered_subject SET approved = True WHERE subjectcode = %s",[it_graderange])
            cursor.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE offered_subject SET approved = True WHERE subjectcode = %s",[it_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[it_codeshare])
                mysql.connection.commit()
            return redirect(url_for('BSIT_Grade_Approved'))
            
    return render_template('bsit_show_grade.html', defult_total_students=defult_total_students, modify_total_students=modify_total_students, CodeshareResult=CodeshareResult, result=result, modify_grade=modify_grade, codeshare_output=codeshare_output)

@app.route('/BSIT_ErrorGrade', methods = ["POST","GET"])
def BSIT_ErrorGrade():
    
    A_max = '100'
    subject_name = ''
    
    it_graderange = session.get('it_graderange')
    meeting_details = session.get('meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[it_graderange])
    subject_name = cursor.fetchall()
    
    if 'set_grade' in request.form:
        cursor.execute("INSERT INTO defult_grade (semester, subjectcode, A_max) VALUES  (%s, %s, %s)", [meeting_details, it_graderange, A_max])
        cursor.execute("INSERT INTO modify_grade (semester, subjectcode, A_min, A_max, A_students, A_minus_min, A_minus_max, A_minus_students, B_plus_min, B_plus_max, B_plus_students, B_min, B_max, B_students, B_minus_min, B_minus_max, B_minus_students, C_plus_min, C_plus_max, C_plus_students, C_min, C_max, C_students, C_minus_min, C_minus_max, C_minus_students, D_min, D_max, D_students, F_min, F_max, F_students, I_min, I_max, I_students, W_min, W_max, W_students) VALUES  (%s, %s, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')", [meeting_details, it_graderange])
        mysql.connection.commit()
        return redirect(url_for('BSIT_SetGrade'))
        
    return render_template('bsit_error_grade.html',subject_name=subject_name)

@app.route('/BSIT_SetGrade', methods = ["POST","GET"])
def BSIT_SetGrade():
    
    A_minus_max = ''
    B_plus_max = ''
    B_max = ''
    B_minus_max = ''
    C_plus_max = ''
    C_max = ''
    C_minus_max = ''
    D_max = ''
    D_min = ''
    F_max = ''
    subject_name_result = ''
    F_min = '0'
    I_min = '-'
    I_max = '-'
    W_min = '-'
    W_max = '-'
    show_gradeRange = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    it_graderange = session.get('it_graderange')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[it_graderange])
    if meeting_offered_subject > 0:
        show_gradeRange = cursor.fetchall()
    
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[it_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
    
    if request.method == 'POST':
        A_min = request.form.get('A_min', type=int)
        A_minus_min = request.form.get('A_minus_min', type=int)
        B_plus_min = request.form.get('B_plus_min', type=int)
        B_min = request.form.get('B_min', type=int)
        B_minus_min = request.form.get('B_minus_min', type=int)
        C_plus_min = request.form.get('C_plus_min', type=int)
        C_min = request.form.get('C_min', type=int)
        C_minus_min = request.form.get('C_minus_min', type=int)
        D_min = request.form.get('D_min', type=int)

        if A_min:
            A_minus_max = A_min - 1
            cursor.execute("UPDATE defult_grade SET A_min = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_minus_max, it_graderange])
            mysql.connection.commit()
            
        if A_minus_min:
            B_plus_max = A_minus_min - 1
            cursor.execute("UPDATE defult_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, it_graderange])
            mysql.connection.commit()
            
        if B_plus_min:
            B_max = B_plus_min - 1
            cursor.execute("UPDATE defult_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, it_graderange])
            mysql.connection.commit()
            
        if B_min:
            B_minus_max = B_min - 1
            cursor.execute("UPDATE defult_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, it_graderange])
            mysql.connection.commit()
            
        if B_minus_min:
            C_plus_max = B_minus_min - 1
            cursor.execute("UPDATE defult_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, it_graderange])
            mysql.connection.commit()
            
        if C_plus_min:
            C_max = C_plus_min - 1
            cursor.execute("UPDATE defult_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, it_graderange])
            mysql.connection.commit()
            
        if C_min:
            C_minus_max = C_min - 1
            cursor.execute("UPDATE defult_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, it_graderange])
            mysql.connection.commit()
            
        if C_minus_min:
            D_max = C_minus_min - 1
            cursor.execute("UPDATE defult_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, it_graderange])
            mysql.connection.commit()
            
        if D_min:
            F_max = D_min - 1
            cursor.execute("UPDATE defult_grade SET D_min = %s, F_min = %s, F_max = %s, I_min = %s, I_max = %s, W_min = %s, W_max = %s WHERE subjectcode = %s",[D_min, F_min, F_max, I_min, I_max, W_min, W_max, it_graderange])
            mysql.connection.commit()
        
        cursor.execute("UPDATE defult_grade SET A_students = '-' WHERE A_students IS NULL")
        cursor.execute("UPDATE defult_grade SET A_minus_students = '-' WHERE A_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_plus_students = '-' WHERE B_plus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_students = '-' WHERE B_students IS NULL")
        cursor.execute("UPDATE defult_grade SET B_minus_students = '-' WHERE B_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_plus_students = '-' WHERE C_plus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_students = '-' WHERE C_students IS NULL")
        cursor.execute("UPDATE defult_grade SET C_minus_students = '-' WHERE C_minus_students IS NULL")
        cursor.execute("UPDATE defult_grade SET D_students = '-' WHERE D_students IS NULL")
        cursor.execute("UPDATE defult_grade SET F_students = '-' WHERE F_students IS NULL")
        cursor.execute("UPDATE defult_grade SET I_students = '-' WHERE I_students IS NULL")
        cursor.execute("UPDATE defult_grade SET W_students = '-' WHERE W_students IS NULL")
            
    if request.method == "POST":
        A_students = request.form.get('A_students', type=int)
        A_minus_students = request.form.get('A_minus_students', type=int)
        B_plus_students = request.form.get('B_plus_students', type=int)
        B_students = request.form.get('B_students', type=int)
        B_minus_students = request.form.get('B_minus_students', type=int)
        C_plus_students = request.form.get('C_plus_students', type=int)
        C_students = request.form.get('C_students', type=int)
        C_minus_students = request.form.get('C_minus_students', type=int)
        D_students = request.form.get('D_students', type=int)
        F_students = request.form.get('F_students', type=int)
        I_students = request.form.get('I_students', type=int)
        W_students = request.form.get('W_students', type=int)
        
        if A_students:
            if request.form.get('A_students') == '0':
                A_students = '-'
                cursor.execute("UPDATE defult_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_graderange])
                mysql.connection.commit()
            
        if A_minus_students:
            if request.form.get('A_minus_students') == '0':
                A_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_graderange])
                mysql.connection.commit()
            
        if B_plus_students:
            if request.form.get('B_plus_students') == '0':
                B_plus_students = '-'
                cursor.execute("UPDATE defult_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, it_graderange])
                mysql.connection.commit()   
            
        if B_students:
            if request.form.get('B_students') == '0':
                B_students = '-'
                cursor.execute("UPDATE defult_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_graderange])
                mysql.connection.commit()
            
        if B_minus_students:
            if request.form.get('B_minus_students') == '0':
                B_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_graderange])
                mysql.connection.commit()
            
        if C_plus_students:
            if request.form.get('C_plus_students') == '0':
                C_plus_students = '-'
                cursor.execute("UPDATE defult_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_graderange])
                mysql.connection.commit()
            else:
                cursor.execute("UPDATE defult_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_graderange])
                mysql.connection.commit()
            
        if C_students:
            if request.form.get('C_students') == '0':
                C_students = '-'
                cursor.execute("UPDATE defult_grade SET C_students = %s WHERE subjectcode = %s", [C_students, it_graderange])
                mysql.connection.commit()
            
        if C_minus_students:
            if request.form.get('C_minus_students') == '0':
                C_minus_students = '-'
                cursor.execute("UPDATE defult_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, it_graderange])
                mysql.connection.commit()
            
        if D_students:
            if request.form.get('D_students') == '0':
                D_students = '-'
                cursor.execute("UPDATE defult_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_graderange])
                mysql.connection.commit()
        
        if F_students:
            if request.form.get('F_students') == '0':
                F_students = '-'
                cursor.execute("UPDATE defult_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_graderange])
                mysql.connection.commit()
                
            else:
                cursor.execute("UPDATE defult_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_graderange])
                mysql.connection.commit()
        
        if I_students:
            if request.form.get('I_students') == '0':
                I_students = '-'
                cursor.execute("UPDATE defult_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_graderange])
                mysql.connection.commit()
        
        if W_students:
            if request.form.get('W_students') == '0':
                W_students = '-'
                cursor.execute("UPDATE defult_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_graderange])
                mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE defult_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_graderange])
                mysql.connection.commit()
            
    return render_template("bsit_setgrade.html", show_gradeRange = show_gradeRange, subject_name_result = subject_name_result, A_minus_max=A_minus_max, B_plus_max=B_plus_max, B_max=B_max, B_minus_max=B_minus_max, C_plus_max=C_plus_max, C_max=C_max, C_minus_max=C_minus_max, D_max=D_max, F_max=F_max)

@app.route('/BSIT_Grade_Approved', methods = ["POST","GET"])
def BSIT_Grade_Approved():

    defult_grade_result = ''
    modify_grade_result = ''
    subject_name_result = ''
    result = ''
    meeting_result = ''
    defult_total_students = ''
    modify_total_students = ''
    
    it_graderange = session.get('it_graderange')
    it_meeting_details = session.get('it_meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    cursor.execute("SELECT SUM(A_students)+SUM(A_minus_students)+SUM(B_plus_students)+SUM(B_students)+SUM(B_minus_students)+SUM(C_plus_students)+SUM(C_students)+SUM(C_minus_students)+SUM(D_students)+SUM(F_students)+SUM(I_students)+SUM(W_students) AS defult_total_student FROM defult_grade WHERE subjectcode = %s",[it_graderange])
    defult_total_student = cursor.fetchone()
    if defult_total_student['defult_total_student'] == defult_total_student['defult_total_student']:
        defult_total_students = int(defult_total_student['defult_total_student'])
    
    cursor.execute("SELECT SUM(A_students)+SUM(A_minus_students)+SUM(B_plus_students)+SUM(B_students)+SUM(B_minus_students)+SUM(C_plus_students)+SUM(C_students)+SUM(C_minus_students)+SUM(D_students)+SUM(F_students)+SUM(I_students)+SUM(W_students) AS total FROM modify_grade WHERE subjectcode = %s",[it_graderange])
    total_student = cursor.fetchone()
    if total_student['total'] == total_student['total']:
        modify_total_students = int(total_student['total'])
        
    modify = cursor.execute("SELECT * FROM modify_grade INNER JOIN subject ON subject.subjectcode = modify_grade.subjectcode WHERE modify_grade.subjectcode = %s",[it_graderange])
    if modify > 0:
        modify_grade_result = cursor.fetchall()
        
    defult = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[it_graderange])
    if defult > 0:
        defult_grade_result = cursor.fetchall()
    
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[it_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
        
    meeting_data = cursor.execute("SELECT * FROM meeting WHERE semester = %s AND program = 'IT'",[it_meeting_details])
    if meeting_data > 0:
        meeting_result = cursor.fetchall()
    
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[it_graderange, it_meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
                
    if request.method == 'POST':
        if request.form['download'] == 'download':
            return redirect(url_for('BSIT_Meeting_Detail'))

    return render_template('bsit_approved_grade.html', meeting_result = meeting_result, defult_total_students = defult_total_students, modify_total_students = modify_total_students, modify_grade_result = modify_grade_result, it_meeting_details = it_meeting_details, subject_name_result = subject_name_result, result=result, defult_grade_result = defult_grade_result)

@app.route("/BSIT_Grade_Change", methods = ["POST","GET"])
def BSIT_Grade_Change():
    
    A_minus_max = ''
    B_plus_max = ''
    B_max = ''
    B_minus_max = ''
    C_plus_max = ''
    C_max = ''
    C_minus_max = ''
    D_max = ''
    D_min = ''
    F_max = ''
    
    show_gradeRange = ''
    subject_name_result = ''
    result = ''
    it_codeshare = ''
    it_l = []
    it_code = ''
    
    it_graderange = session.get('it_graderange')
    it_meeting_details = session.get('it_meeting_details')
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    meeting_offered_subject = cursor.execute("SELECT * FROM defult_grade INNER JOIN subject ON subject.subjectcode = defult_grade.subjectcode WHERE defult_grade.subjectcode = %s",[it_graderange])
    if meeting_offered_subject > 0:
        show_gradeRange = cursor.fetchall()

    #Take Codeshare Subject
    codeshare = cursor.execute("SELECT codeshare_subject FROM codeshare WHERE subjectcode = %s",[it_graderange])
    if codeshare > 0:
        codeshare = cursor.fetchall()
        for output in codeshare:
            if output['codeshare_subject'] == output['codeshare_subject']:
                it_codeshare = output['codeshare_subject']
                it_l.append(it_codeshare)
                print("All codeshare: ", it_l)
                
    subject_name = cursor.execute("SELECT * FROM subject WHERE subjectcode = %s",[it_graderange])
    if subject_name > 0:
        subject_name_result = cursor.fetchall()
        
    codeshare_data = cursor.execute("SELECT subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode = %s and codeshare.semester = %s",[it_graderange, it_meeting_details])
    if codeshare_data > 0:
        result = cursor.fetchall()
        
    if request.method == 'POST':
        
        A_min = request.form.get('A_min', type=int) 
        A_minus_min = request.form.get('A_minus_min', type=int)
        B_plus_min = request.form.get('B_plus_min', type=int)
        B_min = request.form.get('B_min', type=int)
        B_minus_min = request.form.get('B_minus_min', type=int)
        C_plus_min = request.form.get('C_plus_min', type=int)
        C_min = request.form.get('C_min', type=int)
        C_minus_min = request.form.get('C_minus_min', type=int)
        D_min = request.form.get('D_min', type=int)
        
        A_students = request.form.get('A_students')
        A_minus_students = request.form.get('A_minus_students')
        B_plus_students = request.form.get('B_plus_students')
        B_students = request.form.get('B_students')
        B_minus_students = request.form.get('B_minus_students')
        C_plus_students = request.form.get('C_plus_students')
        C_students = request.form.get('C_students')
        C_minus_students = request.form.get('C_minus_students')
        D_students = request.form.get('D_students')
        F_students = request.form.get('F_students')
        I_students = request.form.get('I_students')
        W_students = request.form.get('W_students')
        
        if A_min:
            A_minus_max = A_min - 1
            cursor.execute("UPDATE modify_grade SET A_min = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_minus_max, it_graderange])
            cursor.execute("UPDATE offered_subject SET changed = True WHERE subjectcode = %s",[it_graderange])
            mysql.connection.commit()
            #To change aslo for the Codeshare Grade
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET A_min = %s, A_minus_max = %s WHERE subjectcode = %s", [A_min, A_minus_max, it_codeshare])
                cursor.execute("UPDATE offered_subject SET changed = True WHERE subjectcode = %s",[it_codeshare])
                mysql.connection.commit()
            
        if A_minus_min:
            B_plus_max = A_minus_min - 1
            cursor.execute("UPDATE modify_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET A_minus_min = %s, B_plus_max = %s  WHERE subjectcode = %s",[A_minus_min, B_plus_max, it_codeshare])
                mysql.connection.commit()
            
        if B_plus_min:
            B_max = B_plus_min - 1
            cursor.execute("UPDATE modify_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET B_plus_min = %s, B_max = %s  WHERE subjectcode = %s",[B_plus_min, B_max, it_codeshare])
                mysql.connection.commit()
            
        if B_min:
            B_minus_max = B_min - 1
            cursor.execute("UPDATE modify_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET B_min = %s, B_minus_max = %s  WHERE subjectcode = %s",[B_min, B_minus_max, it_codeshare])
                mysql.connection.commit()
            
        if B_minus_min:
            C_plus_max = B_minus_min - 1
            cursor.execute("UPDATE modify_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET B_minus_min = %s, C_plus_max = %s  WHERE subjectcode = %s",[B_minus_min, C_plus_max, it_codeshare])
                mysql.connection.commit()
            
        if C_plus_min:
            C_max = C_plus_min - 1
            cursor.execute("UPDATE modify_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET C_plus_min = %s, C_max = %s  WHERE subjectcode = %s",[C_plus_min, C_max, it_codeshare])
                mysql.connection.commit()
            
        if C_min:
            C_minus_max = C_min - 1
            cursor.execute("UPDATE modify_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET C_min = %s, C_minus_max = %s  WHERE subjectcode = %s",[C_min, C_minus_max, it_codeshare])
                mysql.connection.commit()
            
        if C_minus_min:
            D_max = C_minus_min - 1
            cursor.execute("UPDATE modify_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET C_minus_min = %s, D_max = %s  WHERE subjectcode = %s",[C_minus_min, D_max, it_codeshare])
                mysql.connection.commit()
            
        if D_min:
            F_max = D_min - 1
            cursor.execute("UPDATE modify_grade SET D_min = %s, F_max = %s WHERE subjectcode = %s",[D_min, F_max, it_graderange])
            mysql.connection.commit()
            
            for it_code in range(len(it_l)):
                it_codeshare = it_l[it_code]
                cursor.execute("UPDATE modify_grade SET D_min = %s, F_max = %s WHERE subjectcode = %s",[D_min, F_max, it_codeshare])
                mysql.connection.commit()

        if A_students:
            if request.form.get('A_students') == '0':
                A_students = '-'
                cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET A_students = %s WHERE subjectcode = %s", [A_students, it_codeshare])
                    mysql.connection.commit()
            
        if A_minus_students:
            if request.form.get('A_minus_students') == '0':
                A_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET A_minus_students = %s WHERE subjectcode = %s", [A_minus_students, it_codeshare])
                    mysql.connection.commit()
            
        if B_plus_students:
            if request.form.get('B_plus_students') == '0':
                B_plus_students = '-'
                cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, it_codeshare])
                    mysql.connection.commit()
            
            else:
                cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_plus_students = %s WHERE subjectcode = %s", [B_plus_students, it_codeshare])
                    mysql.connection.commit()
            
        if B_students:
            if request.form.get('B_students') == '0':
                B_students = '-'
                cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_students = %s WHERE subjectcode = %s", [B_students, it_codeshare])
                    mysql.connection.commit()
            
        if B_minus_students:
            if request.form.get('B_minus_students') == '0':
                B_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET B_minus_students = %s WHERE subjectcode = %s", [B_minus_students, it_codeshare])
                    mysql.connection.commit()
            
        if C_plus_students:
            if request.form.get('C_plus_students') == '0':
                C_plus_students = '-'
                cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_plus_students = %s WHERE subjectcode = %s", [C_plus_students, it_codeshare])
                    mysql.connection.commit()
            
        if C_students:
            if request.form.get('C_students') == '0':
                C_students = '-'
                cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_students = %s WHERE subjectcode = %s", [C_students, it_codeshare])
                    mysql.connection.commit()
            
        if C_minus_students:
            if request.form.get('C_minus_students') == '0':
                C_minus_students = '-'
                cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, cs_graderange])
                mysql.connection.commit()
                
                for cs_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET C_minus_students = %s WHERE subjectcode = %s", [C_minus_students, it_codeshare])
                    mysql.connection.commit()
                    
        if D_students:
            if request.form.get('D_students') == '0':
                D_students = '-'
                cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET D_students = %s WHERE subjectcode = %s", [D_students, it_codeshare])
                    mysql.connection.commit()
        
        if F_students:
            if request.form.get('F_students') == '0':
                F_students = '-'
                cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET F_students = %s WHERE subjectcode = %s", [F_students, it_codeshare])
                    mysql.connection.commit()
        
        if I_students:
            if request.form.get('I_students') == '0':
                I_students = '-'
                cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET I_students = %s WHERE subjectcode = %s", [I_students, it_codeshare])
                    mysql.connection.commit()
        
        if W_students:
            if request.form.get('W_students') == '0':
                W_students = '-'
                cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_codeshare])
                    mysql.connection.commit()
            else:
                cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_graderange])
                mysql.connection.commit()
                
                for it_code in range(len(it_l)):
                    it_codeshare = it_l[it_code]
                    cursor.execute("UPDATE modify_grade SET W_students = %s WHERE subjectcode = %s", [W_students, it_codeshare])
                    mysql.connection.commit()
            
    return render_template("bsit_grade_change.html", show_gradeRange = show_gradeRange, it_meeting_details = it_meeting_details, subject_name_result = subject_name_result, result = result, A_minus_max=A_minus_max, B_plus_max=B_plus_max, B_max=B_max, B_minus_max=B_minus_max, C_plus_max=C_plus_max, C_max=C_max, C_minus_max=C_minus_max, D_max=D_max, F_max=F_max)

@app.route("/BSIT_Delete_GradeRange", methods = ["POST","GET"])
def BSIT_Delete_GradeRange():

    if request.method == 'POST':
        getid = request.form['string']

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('DELETE FROM defult_grade WHERE subjectcode = %s',[getid])
        cur.execute('DELETE FROM modify_grade WHERE subjectcode = %s',[getid])
        cur.execute("UPDATE offered_subject SET approved = False WHERE subjectcode = %s",[getid])
        cur.execute("UPDATE offered_subject SET changed = False WHERE subjectcode = %s",[getid])
        mysql.connection.commit()
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg) 
    
# ------------------------------------------------------------------------------------------------------------------------------
                                                       # OFFER COURSE                                                         
# ------------------------------------------------------------------------------------------------------------------------------

# >> >> Computer Science << <<

#Show BSCS Offered Subjects
@app.route("/BSCS_Offer_Subject", methods = ["POST","GET"])
def BSCS_Offer_Subject():
    
    bscs_sem = ''
    bscs_offered_subjects = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST' and 'sem_search' in request.form:
        sem_search = request.form['sem_search']
        print(sem_search)
        
        bscs_offered = cursor.execute("SELECT offered_subject.subjectcode, subject.subjectname, subject.section FROM offered_subject INNER JOIN subject ON subject.subjectcode = offered_subject.subjectcode WHERE offered_subject.program = 'CS' AND offered_subject.semester = %s ORDER BY subject.subjectname ASC",[sem_search])
        if bscs_offered > 0:
            bscs_offered_subjects = cursor.fetchall()
        else:
            flash("The semester you searched has no offered subjects yet!")
        
        sem_data = cursor.execute("SELECT DISTINCT semester FROM offered_subject WHERE semester = %s",[sem_search])
        if sem_data > 0:
            bscs_sem = cursor.fetchall() 
       
    return render_template('bscs_offered_subject.html', bscs_offered_subjects = bscs_offered_subjects, bscs_sem = bscs_sem)

#Set BSCS Offered Subjects
@app.route("/BSCS_Set_Offer_Subject", methods = ["POST","GET"])
def BSCS_Set_Offer_Subject():
    bscs_subjects = ''
        
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bscs_subject_data = cursor.execute("SELECT * FROM subject WHERE subject.program = 'CS'")
    if bscs_subject_data > 0:
        bscs_subjects = cursor.fetchall()
       
        if request.method == 'POST' and 'selece_semester' in request.form:
            selece_semester = request.form['selece_semester']
            program = "CS"
            approved = False
            changed = False

            checkbox = request.form.getlist('checkbox')
            try:
                for i in checkbox:
                    print(i)
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('INSERT INTO offered_subject (semester, subjectcode, program, approved, changed) VALUES (%s, %s, %s, %s, %s)', (selece_semester, i, program, approved, changed))
                    mysql.connection.commit()
                return redirect(url_for('BSCS_Offer_Subject'))
            
            except:
                flash("Already have in offered subject list please choose other subject!")
                return redirect(url_for('BSCS_Set_Offer_Subject'))

    return render_template('bscs_set_offered_subject.html', bscs_subjects = bscs_subjects)

#Delete BSCS Offered Subjects
@app.route("/BSCS_Delete_OfferSubject", methods = ["POST","GET"])
def BSCS_Delete_OfferSubject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM offered_subject WHERE subjectcode = %s',[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg) 
    
# ------------------------------------------------------------------------------------------------------------------------------

# >> Information Technology Offered Subject <<

#Show BSIT Offered Subjects
@app.route("/BSIT_Offer_Subject", methods = ["POST","GET"])
def BSIT_Offer_Subject():
    
    bsit_sem = ''
    bsit_offered_subjects = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST' and 'sem_search' in request.form:
        sem_search = request.form['sem_search']
        
        bsit_offered = cursor.execute("SELECT offered_subject.subjectcode, subject.subjectname, subject.section FROM offered_subject INNER JOIN subject ON subject.subjectcode = offered_subject.subjectcode WHERE offered_subject.program = 'IT' AND offered_subject.semester = %s ORDER BY subject.subjectname ASC",[sem_search])
        if bsit_offered > 0:
            bsit_offered_subjects = cursor.fetchall()   
        
        else:
            flash("There is no offered subjects yet for your search semester!")
        
        sem_data = cursor.execute("SELECT DISTINCT semester FROM offered_subject WHERE semester = %s",[sem_search])

        if sem_data > 0:
            bsit_sem = cursor.fetchall() 
       
    return render_template('bsit_offered_subject.html', bsit_offered_subjects = bsit_offered_subjects, bsit_sem = bsit_sem)

#Set BSIT Offered Subjects
@app.route("/BSIT_Set_Offer_Subject", methods = ["POST","GET"])
def BSIT_Set_Offer_Subject():
    bsit_subjects = ''
        
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    bsit_subject_data = cursor.execute("SELECT subject.subjectcode, subject.subjectname, subject.section FROM subject LEFT JOIN offered_subject ON offered_subject.subjectcode = subject.subjectcode WHERE offered_subject.subjectcode is NULL AND subject.program = 'IT'")

    if bsit_subject_data > 0:
        bsit_subjects = cursor.fetchall()
       
        if request.method == 'POST' and 'selece_semester' in request.form:
            selece_semester = request.form['selece_semester']
            program = "IT"
            approved = False
            changed = False

            checkbox = request.form.getlist('checkbox')
            try:
                for i in checkbox:
                    print(i)

                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('INSERT INTO offered_subject (semester, subjectcode, program, approved, changed) VALUES (%s, %s, %s, %s, %s)', (selece_semester, i, program, approved, changed))
                    mysql.connection.commit()
                return redirect(url_for('BSIT_Offer_Subject'))
            
            except:
                flash("Already have in Offered Subject For this Semester!")
                return redirect(url_for('BSIT_Set_Offer_Subject'))
        
    return render_template('bsit_set_offered_subject.html', bsit_subjects = bsit_subjects)


#Delete BSIT Offered Subjects
@app.route("/BSIT_Delete_OfferSubject", methods = ["POST","GET"])
def BSIT_Delete_OfferSubject():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM offered_subject WHERE subjectcode = %s',[getid])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
        return jsonify(msg) 
    
# ------------------------------------------------------------------------------------------------------------------------------
                                                     #Set ShareCode Subject                                          
# ------------------------------------------------------------------------------------------------------------------------------

#Set ShareCode
@app.route("/Set_Codeshare", methods = ["POST", "GET"])
def Set_Codeshare():

    subjects = ''
    subjectlists = ''
    
    selectValues = request.form.get('search_filter')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    selectsubject = cursor.execute('SELECT subjectcode,subjectname FROM subject ORDER BY subjectname')
    if selectsubject > 0:
        subjects = cursor.fetchall()
        print(selectValues)

        cursor.execute("SELECT * FROM subject ORDER BY subjectname")
        subjectlists = cursor.fetchall()

        if request.method == 'POST' and 'search_filter' in request.form and 'semester' in request.form:

            search_filter = request.form['search_filter']
            semester = request.form['semester']

            cursor.execute('SELECT semester,subjectcode FROM codeshare WHERE subjectcode = %s and semester = %s', (search_filter, semester))
            getdata = cursor.fetchone()

            # Check if the subject is exisited or not in the same semester.
            if getdata:
                session['setcodeshare'] = True
                session['search_filter'] = getdata['subjectcode']
                session['semester'] = getdata['semester']
                flash('This subject already seted the ShareCode! Please choose other subject.')

            # If subject is not exists in database table record insert data.
            else:
                checkbox = request.form.getlist('checkbox')
                for i in checkbox:
                    print(i)
                    cursor.execute('INSERT INTO codeshare (semester, subjectcode, codeshare_subject) VALUES (%s, %s, %s)', (semester, search_filter, i))
                    mysql.connection.commit()

                return redirect(url_for('search'))

    return render_template('set_codeshare.html', subjects = subjects, subjectlists = subjectlists)

#Search ShareCode Subject
@app.route('/search', methods = ["POST", "GET"])
def search():
    searchresult = ''
    search = ''
    semester = ''
    show_search_result = ''
    heading_result = ''
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    data = cursor.execute("SELECT DISTINCT codeshare.subjectcode, subject.subjectname, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.semester = '1/2022'")
    if data > 0:
        searchresult = cursor.fetchall()
    
    if request.method == 'POST' and 'search' in request.form and 'semester' in request.form:
        search = request.form['search']
        semester = request.form['semester']
                        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        data = cursor.execute("SELECT subject.subjectname, codeshare.subjectcode, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.semester LIKE %s", [semester])
        if data > 0:
            searchresult = cursor.fetchall()
            
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        data = cursor.execute("SELECT subject.subjectname, codeshare.subjectcode, codeshare.codeshare_subject FROM codeshare INNER JOIN subject ON subject.subjectcode = codeshare.codeshare_subject WHERE codeshare.subjectcode LIKE %s", [search])
        if data > 0:
            searchresult = cursor.fetchall()
            
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        show_search = cursor.execute("SELECT DISTINCT subject.subjectname FROM subject INNER JOIN codeshare ON subject.subjectcode = codeshare.subjectcode WHERE subject.subjectcode LIKE %s",[search])
        if show_search > 0:
            show_search_result = cursor.fetchall()

    return render_template('search.html', heading_result = heading_result, searchresult = searchresult, search = search, semester = semester, show_search_result = show_search_result)

@app.route("/Codeshare_Delete", methods = ["POST","GET"])
def Codeshare_Delete():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']

        cur.execute('DELETE FROM codeshare WHERE codeshare_subject = %s',[getid])
        mysql.connection.commit()
        cur.close()
        msg = 'Record deleted successfully'
        return jsonify(msg) 
# ------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
    