

from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="py_db"
)

cursor = connection.cursor()

query = "select * from sports"

cursor.execute(query)

# fetchall is used to retrieve or fetch all records in that table to a variable records
records = cursor.fetchall()

# iterting all the records available in that table
for row in records:

    print(row)

cursor.close()
connection.close()