db_pin = "1234"

user_pin = input("enter a pin=")

balance = 5000

if db_pin==user_pin:

    withdrawal_amount = int(input("enter a withdrawal amount="))

    if withdrawal_amount<=balance:

        print("withdrawal successful")
        account_balance= balance-withdrawal_amount
        print("account balance=",account_balance)
    else:
        print("insufficient balance")
        account_balance= balance-withdrawal_amount
        print("account balance=",account_balance)
        
        
else:

    print("incorrect pin")