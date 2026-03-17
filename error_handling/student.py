

"""

Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally


"""
try:
     name = input("enter a name=")
     course_fee = int(input("enter course fee="))
     amount_paid = int(input("enter amount paid="))

     if course_fee<0:

        raise Exception ("course fee is negative")

     elif amount_paid<0:

       raise Exception("amount paid is negative")
     
     elif amount_paid>course_fee:

        raise Exception("amount paid is greater than course fee")
     
except Exception as e:
   
   print(e)

finally:
   
   print("registration process finished")








