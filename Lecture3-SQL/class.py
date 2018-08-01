class Flight:

	def __init__(self , origin , destination , duration):
		self.origin = origin
		self.destination = destination
		self.duration = duration


	def print_details(self):
		print(f"Flight origin : {self.origin}")
		print(f"Flight destination : {self.destination}")
		print(f"Flight duration : {self.duration}")


def main():
	#Create flight
	f = Flight(origin = "New York" , destination =  "Paris" , duration = 520)
	f.print_details()
	f.duration += 10 #change duration

	
	f2 = Flight(origin = "New York" , destination =  "Dubai" , duration = 5200)
	f2.print_details()

if __name__ == "__main__":
	main()