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
    userdata = dict(request.form)
    user = userdata["username"]
    password = userdata["password"]
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=",")
        first_line = True
        users = []
        if not first_line:
            if (row[0].strip() == user.strip() & row[1].strip() == password.strip()):
                return render_template("index.html")
            else:
                return render_template("signin.html")
        else:
            first_line = False
    return render_template("index.html")
        
    


