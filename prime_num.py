#Print First N Prime Numbers

a = int(input("Enter a number: "))
print("The first n prime numbers are: ")
def prime_num(x):
	i = 2
	count = 0
	while count < x:
		for b in range(2, i):
			if i % b == 0:
				break
		else:
			print(i)
			count += 1
		i += 1
prime_num(a)

