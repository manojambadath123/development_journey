

from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="v_db"
)

cursor = connection.cursor()

query = "update vehicle set model=%s where id =%s"

data = ("Etios",1)

cursor.execute(query,data)

connection.commit()


cursor.close()
connection.close()

print("record updated...")

