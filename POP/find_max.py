num = [12, 3, 7, 4, 9, 13, 6]
a = len(num)
def find_max(number):
	max = number[0]
	for i in range(1, a):
		if number[i] > max:
			max = number[i]
	print(max)
find_max(num)