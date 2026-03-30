

from mysql import connector

connection = connector.connect(

host = "localhost",
user = "root",
password="Password@123",
database = "v_db"

)

cursor = connection.cursor()

query = """

insert into vehicle (name,model,running_km,fuel_type,owner_type,place,owner) values (%s,%s,%s,%s,%s,%s,%s)

"""
# data in tuple(so that it cannot be changed its immutable) will move to the place holder %s
data = ("Maruti", "Swift", 40000, "Diesel", "Third Owner", "Trivandrum", "Arun")

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("data inserted...")