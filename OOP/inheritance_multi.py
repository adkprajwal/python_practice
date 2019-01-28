class A:
	def __init__(self):
		print("Inside init of A")

	def feature(self):
		print("I am feature of A")

	def feature_a1(self):
		print("I am feature_a1")

	def feature_a2(self):
		print("I am feature_a2")

class B:
	def __init__(self):
		print("Inside init of B")

	def feature(self):
		print("I am feature B")

	def feature_b1(self):
		print("I am feature_b1")

	def feature_b2(self):
		print("I am feature_b2")

class C(A, B):

	"""If you donot explicitly declare constructor(__init__) of C, the object of C automatically calls 
	constructor of A as C inherits A But if you declare the constructor(__init__) of C then the object of C calls its 
	own constructor(__init__)
	By using super keyword you can call init of super class(A in this case) even if you have explicitly declared init
	in the subclass
	In  this case even if C inherits both A and B the super keyword creates constructor of A because of sumething called
	Method Resolution Order(MRO). In inheritance it always works from left to right. Since A is written before B the
	constructor of  A is called before B. This is same for methods too."""
	def __init__(self):
		super().__init__()
		print("Inside init of C")

	def feat(self):
		super().feature()

	# def feat(self, other):
	# 	other.feature()

	def feature_c1(self):
		print("I am feature_c1")

	def feature_c2(self):
		print("I am feature_c2")

print("")
a = A()
a.feature_a1()
a.feature_a2()

print("")
b = B()
b.feature_b1()
b.feature_b2()

print("")
c = C()
c.feat()
# c.feat(b)
c.feature_a1()
c.feature_a2()
c.feature_b1()
c.feature_b2()
c.feature_c1()
c.feature_c2()



