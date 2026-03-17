

bank = {"account_number":12345,"holder_name":"vipin","balance":5000}

print(bank)

bank["balance"]+=5000

print(bank)

if bank["balance"]>2000:
    
    bank["balance"]-=2000

else:

    print("insufficient balance")

print(bank)

if bank["balance"]< 1000:

    print("low balance")

else:

    print("sufficient balance")

