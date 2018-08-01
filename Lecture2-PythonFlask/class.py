
class Passenger:


	def __init__(self , name):
		self.name = name 


class Flight:

	counter = 1

	def __init__(self , origin , destination , duration):
		
		self.id = Flight.counter #keep track of id number
		Flight.counter += 1

		self.passengers = []
		#keep track of passengers

		#keep track of flight details
		self.origin = origin
		self.destination = destination
		self.duration = duration


	def print_details(self):
		print(f"Flight origin : {self.origin}")
		print(f"Flight destination : {self.destination}")
		print(f"Flight duration : {self.duration}")


		print()
		print("Passengers:")
		for passenger in self.passengers:
			print(f"{passenger.name}")

	def delay(self , amount):
		self.duration += amount



	def add_passenger(self , p):
		self.passengers.append(p)
		p.flight_id = self.id 





def main():
	#Create flight
	f = Flight(origin = "New York" , destination =  "Paris" , duration = 520)
	f.print_details()
	f.delay(10) #change duration

	
	f2 = Flight(origin = "New York" , destination =  "Dubai" , duration = 5200)
	f2.delay(20)
	f2.print_details()

	alice = Passenger(name = "Alice")
	bob = Passenger(name = "Bob")

	f2.add_passenger(alice)
	f.add_passenger(bob)

	f.print_details()
	f2.print_details()

if __name__ == "__main__":
	main()