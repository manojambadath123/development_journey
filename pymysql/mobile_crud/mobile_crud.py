from mysql import connector

class MobileListRetrieveCreateUpdateDelete:

    def __init__(self):

        try:

               self.connection = connector.connect(

                    host = "localhost",
                    user="root",
                    password = "Password@123",
                    database="mobile_db"

                   )

               self.cursor = self.connection.cursor()

               print("db connection ok...")

        except Exception as e:
             
               print(e)
    
    def list(self):
          
             query = "select * from mobile"

             self.cursor.execute(query)

             records = self.cursor.fetchall()

             if records:
                
                 for row in records:
                     print(row)
             else:
                
                print("no records found")

    def create(self,title=None,brand=None,specs=None,price=None):
         
                query ="""
                       insert into mobile (title,brand,specs,price) values (%s,%s,%s,%s)

                    """
                data = (title,brand,specs,price)

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted")

    def retrieve(self,id=None):
          
                query = " select * from mobile where id =%s"

                data = (id,)

                self.cursor.execute(query,data)

                record = self.cursor.fetchone()

                if record:
                       
                       print(record)

                else:
                       print("no records found")

    

    def delete(self,id=None):
           
                query = " delete from mobile where id=%s"

                data = (id,)

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record deleted...")

    def update(self,title=None,id=None):
           
               query = "update mobile set title=%s where id =%s "

               data = (title,id)

               self.cursor.execute(query,data)

               self.connection.commit()

               print("record updated...")

           

mobile_instance = MobileListRetrieveCreateUpdateDelete()
mobile_instance.list()
# mobile_instance.create(title="iPhone 14",brand="Apple",specs="6GB RAM,128GB Storage,A15 Bionic,6.1-inch Display",price=75000)
# mobile_instance.create(title="Galaxy S23",brand="Samsung",specs="8GB RAM,256GB Storage,Snapdragon 8 Gen 2,6.1-inch Display",price=74000)
# mobile_instance.create(title="Pixel 7",brand="Google",specs="8GB RAM,128GB Storage,Google Tensor G2,6.3-inch Display",price=73000)


# mobile_instance.retrieve(id=1)
# mobile_instance.delete(id=3)
# mobile_instance.update(title="iPhone 16",id=1)

