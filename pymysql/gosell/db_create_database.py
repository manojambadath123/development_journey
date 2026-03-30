
from mysql import connector
# created connection object to make or establish connection
connection = connector.connect(

host = "localhost",
user = "root",
password = "Password@123"

)
# created cursor object to execute query
cursor = connection.cursor()
#query specified in the form of string in python
query = "create database v_db"
# executing query using cursor
cursor.execute(query)
#change apply since we are not reading we are creating database so we need to commit the connection for applying change (create or update)
connection.commit()

print("completed")