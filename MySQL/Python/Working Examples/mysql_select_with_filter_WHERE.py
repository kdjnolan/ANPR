import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

#Select record(s) where the registration number IS...
sql = "SELECT * FROM users WHERE registration ='99D4545'"

#Select record(s) where the name CONTAINS 'john'...
#sql = "SELECT * FROM users WHERE name LIKE '%way%'"

#When query values are provided by the user, escape the values
#sql = "SELECT * FROM users WHERE address = %s"
#adr = ("street", )
#mycursor.execute(sql, adr)


mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
