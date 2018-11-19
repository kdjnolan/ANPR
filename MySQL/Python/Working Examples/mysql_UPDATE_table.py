import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

#sql = "UPDATE users SET address = 'Street 1' WHERE address = 'Street 100'"
#mycursor.execute(sql)



#prevent sql injection with %s placeholder
sql = "UPDATE users SET address = %s WHERE address = %s"
val = ("Street 1", "Street 100")

mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, "record(s) affected")
