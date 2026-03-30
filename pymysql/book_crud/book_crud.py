

from mysql import connector

class BookListRetrieveCreateUpdateDelete:

    def __init__(self):

        try:

               self.connection = connector.connect(

                    host = "localhost",
                    user="root",
                    password = "Password@123",
                    database="book_db"

                   )

               self.cursor = self.connection.cursor()

               print("db connection ok...")

        except Exception as e:
             
               print(e)
    
    def list(self):
          
             query = "select * from book"

             self.cursor.execute(query)

             records = self.cursor.fetchall()

             if records:
                
                 for row in records:
                     print(row)
             else:
                
                print("no records found")

    def create(self,title=None,author=None,price=None,publisher=None,genre=None,year=None):
         
                query ="""
                       insert into book (title,author,price,publisher,genre,year) values (%s,%s,%s,%s,%s,%s)

                    """
                data = (title,author,price,publisher,genre,year)

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted")

    def retrieve(self,id=None):
          
                query = " select * from book where id =%s"

                data = (id,)

                self.cursor.execute(query,data)

                record = self.cursor.fetchone()

                if record:
                       
                       print(record)

                else:
                       print("no records found")

    

    def delete(self,id=None):
           
                query = " delete from book where id=%s"

                data = (id,)

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record deleted...")

    def update(self,title=None,id=None):
           
               query = "update book set title=%s where id =%s "

               data = (title,id)

               self.cursor.execute(query,data)

               self.connection.commit()

               print("record updated...")

           

book_instance = BookListRetrieveCreateUpdateDelete()
book_instance.list()
# book_instance.create(title="randamoozham",author="mt",price=580,publisher="dcbooks",genre="fiction",year="1997")
# book_instance.create(title="pazhassiraja",author="mt",price=590,publisher="dcbooks",genre="fiction",year="1995")

# book_instance.retrieve(id=1)
# book_instance.delete(id=6)
# book_instance.update(title="pazhassiraja",id=1)

