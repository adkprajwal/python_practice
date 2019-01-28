class Computer:
	def __init__(self):
		self.name = "Prajwal"
		self.age = 21

	def update(self, other):
		self.name = "Machha"
		other.age = 20

	def compare(self, other):
		if self.age == other.age:
			return True
		else:
			return False

c1 = Computer()
c2 = Computer()

c2.name = "Sagar"
c2.age = 22

c1.update(c2)

print("Name and age of first object: ")
print(c1.name)
print(c1.age)

print("Name and age of second object: ")
print(c2.name)
print(c2.age)

if c1.compare(c2):
	print("Both have same age.")
else:
	print("Both dont have same age.")


