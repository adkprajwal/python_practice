class Student:

	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap1 = self.Laptop()

	def show(self):
		print(self.name, self.rollno)
		self.lap1.show()


	class Laptop:

		def __init__(self):
			self.brand = "ACER"
			self.cpu = "i5"
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)

s1 = Student("Prajwal", 27)
s2 = Student("Gharmi", 31)
s1.show()
s2.show()

		
		