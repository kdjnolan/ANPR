import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users WHERE name = 'John Evans'"#remove WHERE to delete all records

# To prevent sql injections use the %s placeholder...
'''
sql = "DELETE FROM users WHERE address = %s"
adr = ("Street 1", )

mycursor.execute(sql, adr)
'''

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

