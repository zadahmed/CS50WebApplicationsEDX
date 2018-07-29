#flask application using sql and python
import os

from flask import Flask , render_template , request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind = engine))

app = Flask(__name__)

@app.route("/")
def index():
	flights = db.execute("SELECT * FROM flights").fetchall()
	return render_template("index.html" , flights = flights)

@app.route("/book" methods = ["POST"])
def book():

	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html" , message = "Invalid Flight Number")

	if db.execute("SELECT * FROM flights WHERE id = :id" ,{ "id":flight_id).row_count == 0:
		render_template("error.html" , message = "no flight exists")
	db.execute("INSERT INTO passengers (name , flight_id) VALUES (:name , :flight_id)",{"name":name , "flight_id" : flight_id})
	db.commit()
	retuurn render_template("success.html")