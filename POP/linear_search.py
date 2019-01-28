my_array = [12, 45, 67, 34, 97, 27]
a = int(input("Enter an element to search: "))
l = len(my_array)
flag = 0;
for x in range(l):
	if my_array[x] != a:
		x += 1
	elif my_array[x] == a:
		print("Element found at index %s" %x)
		flag = 1;
		break
else:
	if flag == 0:
		print("Element not found.")


