from flask import Flask , render_template , request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	db.create_all()
	# to delete a flight from database
	# flight1 = Flight.query.get(id)
	#db.session.delete(flight)


	#to order flights
	#Flight.query.order_by(Flight.origin.desc()).all()


	#fliter flights
	# Flight.query.filter(Flight.origin.like("%a%")).all()
	
if __name__ == "__main__":
	with app.app_context():
		main()

