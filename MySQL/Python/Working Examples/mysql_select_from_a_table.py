#script to select the 'registration' and 'name' columns

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="mypidatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM users")
# To select all columns 
# mycursor.execute("SELECT * FROM customers")


# To return only the first row use fetchone() method
# myresult = mycursor.fetchone()

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
