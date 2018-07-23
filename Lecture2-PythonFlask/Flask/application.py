from flask import Flask,render_template
import datetime


app = Flask(__name__)

@app.route("/")
def index():
	headline = "Welcome"
	return render_template("index.html" , headline = headline)

@app.route("/zahid")
def zahid():
	return "Hello Zahid!"

@app.route("/<string:name>") #takes any string after the slash and say hello
def hello(name):
	name = name.capitalize()
	return f"<h1>Hello,{name}!</h1>"



@app.route("/newyear")
def newyear():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	return render_template("index.html" , new_year = new_year)