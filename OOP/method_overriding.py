class Father:
	def phone(self):
		print("Has a nokia phone")

class Son(Father):
	def phone(self):
		print("Has a motorola phone")

s1 = Son()
s1.phone()