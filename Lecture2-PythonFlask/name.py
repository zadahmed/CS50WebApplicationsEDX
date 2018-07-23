name = input()
print(f"hello, {name}!")

l = set()
l.add(1)
l.add(2)
print(l)

def square(x):
	return x*x

def main():
	for i in range(10):
		print("{} squared is {}".format(i , square(i)))

if __name__ == "__main__":
	main()

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y


p = Point(3,5)
print(p.x)
print(p.y)

