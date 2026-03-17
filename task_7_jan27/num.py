
# def check_num_sign(number):
#        if number>0:
#               return 1
#        elif number<0:
#               return 2
#        else:
#               return 3

# num = int(input("enter a number="))
# sign_value = check_num_sign(num)

# match sign_value:

#     case 1:           
#             print(num,"is positive")
#     case 2:
#             print(num,"is negative")
#     case 3:
#             print(num,"is zero")


number = int(input("enter number="))

match number:

       case 0:
              print("zero")
       case _ if number<0:print("-ve")

       case _ if number>0:print("-ve")

       case _:
              print("invalid")