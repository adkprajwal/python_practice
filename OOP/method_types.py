class Student:

	school = 'Ryba University'

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 + self.m2 + self.m3)/3

		#Getters/Accessors

	def get_m1(self):
		return self.m1

		#Setters/Mutators

	def set_m1(self, value):
		self.m1 = value
	
	@classmethod
	def getSchool(cls):
		return cls.school

	@staticmethod		#Works with everything except class or instance variable.
						# Used when we have to work with something extra.
	def info():
		print("	This is a student class in abc module.")

s1 = Student(50,43,64)
s2 = Student(65,70,45)

#Accessing the m1 variable through getter.
#This method is used if we want to access any private variable outside the class scope.
print(Student.getSchool())
print("")
print(s1.get_m1())		
#Directly accessing the m2 variable				
print(s1.m2)	
#Directly accessing the m3 variable	
print(s1.m3)		
print("Average of object 's1' is %s" %s1.avg())


print("")
 	
print(s2.get_m1())					
print(s2.m2)	
print(s2.m3)		
print("Average of object 's2' is %s" %s2.avg())
Student.info()