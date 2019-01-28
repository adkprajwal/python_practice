# PRINTING FIBONACCI NUMBERS IN ITERATIVE WAY
import time

num = int(input("Enter the number of terms: "))
start_time = time.clock()
a = 0
b = 1
print(a)
print(b)
for x in range(num-2):
	c = a + b
	print(c)
	a = b
	b = c
end_time = time.clock()
print("Execution time: %s"%(end_time-start_time))

