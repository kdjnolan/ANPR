import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (registration, name, address) VALUES (%s, %s, %s)"
data = ("96G6767", "Jim", "Galway")

mycursor.execute(sql, data)

mydb.commit()				#makes the changes

print(mycursor.rowcount, "record inserted.")
