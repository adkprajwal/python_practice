import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")
# mycursor.execute("CREATE DATABASE demo")
#mycursor.execute("CREATE TABLE table_demo (roll int, name varchar(255), address varchar(255))")
mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
sql = "INSERT INTO table_demo (roll, name, address) VALUES (%s, %s, %s)"
val = ("27", "Prajwal", "Lakeside 6")
mycursor.execute(sql, val)
mydb.commit()