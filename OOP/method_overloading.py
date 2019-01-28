class Student:

	def __init__(self):
		pass

	def sum(self, a=None, b=None, c=None):
		if a!=None and b!=None and c!=None:
			return a + b + c
		elif a!=None and b!=None and c==None:
			return a + b
		else:
			return a

s1 = Student()
s2 = Student()
s3 = Student()
m = s1.sum(5, 6, 7)
n = s2.sum(4, 3)
o = s3.sum(9)
print(m, n, o)