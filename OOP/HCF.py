class HCF:
	i = 1

	#Checking the factors and storing all of it in an array
	def check_factors(self, a):
		arr = []
		i = self.i
		while(i <= a):
			if (a % i == 0):
				arr.append(i)
			i += 1
		return arr

	#Comparing the list of factors of given two numbers
	def compare(self, m, n):
		m = sorted(m, reverse = True)
		for x in m:
			if x in n:
				return x
				break

print("\nEnter any two numbers: ")
num1 = int(input())
num2 = int(input())

h1 = HCF()
h2 = HCF()
h3 = HCF()

list1 = h1.check_factors(num1)
list2 = h2.check_factors(num2)
hcf = h3.compare(list1, list2)

print("\nThe factors of given numbers are:")
print("%s:	%s" %(num1, list1))
print("%s:	%s" %(num2, list2))
print("The HCF is: %s" %hcf)





