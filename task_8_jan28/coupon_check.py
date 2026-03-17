
db_coupon_code = "abc123"

user_coupon_code = input("enter a coupon code=")

if db_coupon_code==user_coupon_code:

    cart_amount = int(input("enter a cart amount="))
    if cart_amount>=1000:

        print("coupon applied")

    else:

        print("minimum purchase not met")
else:

    print("invalid coupon")

