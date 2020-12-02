from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, static_url_path='')

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/student', methods=["GET","POST"])
def student_page():
    if request.method == "POST":
        insertStudentData(request.form['rno'], request.form['sname'], request.form['dob'], request.form['cid'])
        print("Data stored into database")
        # return render_template('home.html')
    return render_template('student.html')

@app.route('/admin', methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        insertCourseData(request.form['cid'], request.form['cname'], request.form['dur'], request.form['fee'])
        print("Data stored into database")
        # return render_template('home.html')
    return render_template('admin.html')


@app.route('/api/courses', methods=["GET"])
def getCoursesMap():
    courses = getCourses()
    return {'courses': courses}

@app.route('/api/students', methods=["GET"])
def getStudentsMap():
    students = getStudents()
    return {'students': students}



def insertStudentData(rno, name, dob, cid):
    sqlstr = 'INSERT INTO student VALUES(%s, %s, %s, %s);'
    val = (rno, name, dob, cid)
    cur.execute(sqlstr, val)
    mydb.commit()

def insertCourseData(cid, name, dur, fee):
    sqlstr = 'INSERT INTO course VALUES(%s, %s, %s, %s);'
    val = (cid, name, dur, fee)
    cur.execute(sqlstr, val)
    mydb.commit()

def getCourses():
    sqlstr = "SELECT * FROM course"
    cur.execute(sqlstr)
    res = cur.fetchall()
    return res

def getStudents():
    sqlstr = "SELECT rollno, name, courseid FROM student"
    cur.execute(sqlstr)
    res = cur.fetchall()
    return res

### ------------------------ ###
mydb = mysql.connector.connect(
  host="localhost", 
  user="root",  #db username here
  password="",  #db password here
  database = "sample-flask" # database name here
)
cur = mydb.cursor()

app.run(debug="True")