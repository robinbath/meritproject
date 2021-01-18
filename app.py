from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users')
def return_users():
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                users.append({
                "Username": row[0],
                "Password": row[1],
                })
            else:
                first_line = False
    return render_template("index.html", users=users)

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")
    
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 != users[0]:
	    return render_template('signin.html',info='Invalid User')
    else:
        if users[name1]!=pwd:
            return render_template('signin.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=name1)
    return render_template("signin.html")

@app.route('/getUser', methods=["POST"])
def return_users_by_city():
    userdata = dict(request.form)
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                if( row[2].strip() == city.strip() ):
                    users.append({
                    "Username": row[0],
                    "Password": row[1]
                    })
            else:
                first_line = False
    if( len(users) == 0 ):
        status = "Invalid login."
    else:
        status = "Welcome!"
    return render_template("index.html", status=status, users=users)

