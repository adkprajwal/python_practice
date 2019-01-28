a = 5
b = 0

try:
	fil = open("file.txt", "r+")
	str = fil.read(30)
	print(str)
	c = a / b
	print(c)
	num = int(input("Enter a number: "))
	fil = open("foo.txt", "r")
except ZeroDivisionError as e:
	print("Cannot divide a number by zero")
except ValueError as e:
	print("Invalid Input")
except Exception as e:
	print("Something went wrong")

finally:
	fil.close()

