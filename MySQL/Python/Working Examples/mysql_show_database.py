import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root"
	database="mypidatabase"#try to connect to database
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)
