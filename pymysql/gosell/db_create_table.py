

from mysql import connector

connection = connector.connect(

host = "localhost",
user = "root",
password = "Password@123",
database = "v_db"

)

cursor = connection.cursor()
# since it is multiple line query use doc string quotes
query = """ 

create table vehicle (
id int auto_increment primary key,
name varchar(200) not null unique,
model varchar(100),
running_km int,
fuel_type varchar(100),
owner_type varchar(100),
place varchar(100),
owner varchar(100)
)

"""

cursor.execute(query)

connection.commit()

print("table created")

# these codes will come under finally
cursor.close()
connection.close()