#Print First N Prime Numbers and find execution time of the program.
import time
a = int(input("Enter a number: "))
start_time = time.clock()
print("The first n prime numbers are: ")
def prime_num(x):
	i = 2
	result = []
	count = 0
	while count < x:
		for b in range(2, i):
			if i % b == 0:
				break
		else:
			#result.append(i)
			print(i)
			count += 1
		i += 1
	#print(result)
prime_num(a)
print("%s seconds" %(time.clock() - start_time))

