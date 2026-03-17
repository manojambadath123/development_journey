
purchase_amount = int(input("enter your purchase amount="))

if purchase_amount>5000:
    print("20% discount")
    discount = 20/100*purchase_amount
    print(discount)
    purchase_org_amount=purchase_amount-discount
    print(purchase_org_amount)

elif purchase_amount>=2000 and purchase_amount<=5000:
    print("10% discount")
    discount = 10/100*purchase_amount
    print(discount)
    purchase_org_amount=purchase_amount-discount
    print(purchase_org_amount)

elif purchase_amount<2000:
    print("No discount")
    purchase_org_amount = purchase_amount
    print(purchase_org_amount)




