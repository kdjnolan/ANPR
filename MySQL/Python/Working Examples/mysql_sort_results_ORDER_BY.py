import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

#sort results alphabetically by name (default is ascending order)
sql = "SELECT * FROM users ORDER BY name"

#sql = "SELECT * FROM users ORDER BY name DESC"  #sort in descending order

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
