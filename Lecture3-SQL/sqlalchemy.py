#sqlalchemy connect python and sql

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session , sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind = engine))


def main():
	#List All flights
	flights = db.execute("SELECT  id , origin , destination , duration FROM flights").fetchall()
	for flight in flights:
		print(f"{flight.id} : {flight.origin} to {flight.destination} , {flight.duration} minutes.")


	#Prompt user to choose a flight
	flight_id = int(input("\nFlight ID:"))
	flight = db.execute("SELECT origin , destination , duration FROM flights WHERE id = :id")
	{"id": flight_id}).fetchone()

	
	if flight is None:
		print("Error : No Such Flight")
		return

	#List passengers
	passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id ")
	{"flight_id": flight_id}.fetchall()

	print("\n Passenger:")
	for passenger in passengers:
		print(passenger.name)
	if len(passengers) == 0:
		print("No Passengers.")

if __name__ = "__main__":
	main()


def forcsvfiles():
	f = open("flights.csv")
	reader = csv.reader(f)
	for origin , destination , duration in reader:
		db.execute("INSERT INTO flights ( origin , destination , duration ) VALUES (:origin , :destination , :duration)",
			{"origin": origin ,"destination": destination,"duration" :duration })
		print(f"Added Flight from {origin} to {destination} lasting {duration} minutes")
	db.commit() 