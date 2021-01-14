from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")