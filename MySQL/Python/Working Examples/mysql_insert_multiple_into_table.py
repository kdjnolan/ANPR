import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypidatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (registration, name, address) VALUES (%s, %s, %s)"
val = [
	('99D555', 'James', 'Street 4'),
	('92S2335', 'John', 'Street 10'),
	('99G4545', 'Mary', 'Shit Street')
]

mycursor.executemany(sql, val)

mydb.commit()

# Return the number of rows inserted
print(mycursor.rowcount, "was inserted.")


# To return the ID of the row that was inserted...
#print("1 record inserted, ID:", mycursor.lastrowid) 
