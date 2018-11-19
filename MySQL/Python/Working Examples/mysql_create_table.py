#python script to create a table called 'users'
#in a database called 

#also need to create a column with a unique key for each record (PRIMARY KEY)

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="mypidatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users 
	(id INT AUTO_INCREMENT PRIMARY KEY,
	registration VARCHAR(255), name VARCHAR(255), address VARCHAR(255))")

# If table already exists we can add primary key with 'ALTER TABLE'
#mycursor.execute("ALTER TABLE USERS ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
	

# now check if the table was created
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)
