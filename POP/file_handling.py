fil = open("file.txt", "a+")
fil.write("This is newly created file with python file handling.")
fil.write("Ram")
str = fil.read()
print("Read string is: ", str)
fil.close()
print ("Name of the file: ", fil.name)
print ("Closed or not : ", fil.closed)
print ("Opening mode : ", fil.mode)
