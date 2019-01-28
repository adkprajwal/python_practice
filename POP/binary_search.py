import time
import random

start_time = time.perf_counter()

#RANDOM LIST GENERATOR
my_array = list()
for x in range(1000):
	my_array.append(random.randint(1, 20001))
print("\nThis is a randomly generated list: \n\n %s"%my_array)

mid_time1 = time.perf_counter()

#INPUT ELEMENT TO SEARCH
num = int(input("\nEnter an element to search: "))

mid_time2 = time.perf_counter()
l = len(my_array)					#GETTING LENGTH OF ARRAY
sorted_array = sorted(my_array)		#SORTING
print("\nThe sorted list is: \n\n %s"%sorted_array)


#BINARY SEARCH ALGORITHM
start = 0
end = l - 1
flag = 0
while start < end:
	mid = (start + end)//2
	if sorted_array[mid] < num:
		start = mid + 1
	elif sorted_array[mid] > num:
		end = mid - 1
	elif sorted_array[mid] == num:
		print("\nThe required element is found at index %s"%mid)
		flag = 1
		break
if flag == 0:
	print("\nThe Element is not found")

end_time = time.perf_counter()
exec_time = end_time - start_time - (mid_time2 - mid_time1)		#CALCULATING PROGRAM EXECUTION TIME
print("\nExecution time is: \n %s second"%(exec_time))
