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
    
@app.route('/fantasy')
def fantasy():
    return render_template("fantasy.html")

@app.route('/clockworkangel')
def clockworkangel():
    return render_template("clockworkangel.html")

@app.route('/contemporary')
def contemporary():
    return render_template("contemporary.html")

@app.route('/allthebrightplaces')
def allthebrightplaces():
    return render_template("allthebrightplaces.html")
@app.route('/community')
def community():
    with open('data/topic1.csv') as file:
        data = csv.reader(file, delimiter=',')
        firstline = True
        topics = []
        for row in data:
            if not firstline:
                topics.append({
                    "username": row[0],
                    "comments": row[1]
                })
            else:
                firstline = False
    return render_template("community.html", topics=topics)
    
@app.route('/community', methods=["GET", "POST"])
def submit_comment():
    if request.method == "GET":
        return redirect(url_for('community'))
    elif request.method == "POST":
        commentdata = dict(request.form)
        username = commentdata["username"]
        comments = commentdata["comments"]
        if(len(username) < 1 or len(comments) < 1):
            return render_template("community.html", status='name/comments too short')
        else:
            with open('data/topic1.csv', mode='a', newline='') as file:
                data = csv.writer(file)
                data.writerow([username, comments])
            #return render_template("community.html", status='sent!') 
            return redirect(url_for('community'))

@app.route('/about')
def about():
    return render_template("about.html")
    
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
        


