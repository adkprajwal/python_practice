import time

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
start_time = time.clock()
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
end_time = time.clock()
print("Execution time: %s"%(end_time-start_time))
