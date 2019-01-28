class Shape:
	def display(self):
		print("I am a function of parent class.")
		
	def draw(self):
		print("\nI am a shape.")

class Rectangle(Shape):
	def draw(self):
		print("\nI am a Rectangle.")

	def area_rec(self):
		print("Area = length * breadth")

class Square(Shape):
	def draw(self):
		print("\nI am a Square.")

	def area_sq(self):
		print("Area = length * length")

class Circle(Shape):
	def draw(self):
		print("\nI am a Circle.")

	def area_cir(self):
		print("Area = πr^2")

sh = Shape()
sh.draw()

rec = Rectangle()
rec.display()
rec.draw()
rec.area_rec()

sq = Square()
sq.display()
sq.draw()
sq.area_sq()

cir = Circle()
cir.display()
cir.draw()
cir.area_cir()
	