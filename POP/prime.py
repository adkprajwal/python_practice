#Print Prime Numbers below input value

num = int(input("Enter a number below which you want to find the prime numbers: "))
def prime_num(x):
	for i in range(2, x):
		for b in range(2, i):
			if i % b == 0:
				break 	
		else:
			print(i)
prime_num(num)