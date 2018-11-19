import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

#select first 4 results
#mycursor.execute("SELECT * FROM users LIMIT 4")

#start at position 4 and return 5 records
mycursor.execute("SELECT * FROM users LIMIT 5 OFFSET 3")#(1+3=4)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
