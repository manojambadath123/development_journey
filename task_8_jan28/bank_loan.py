
monthly_income = int(input("enter monthly income="))

if monthly_income>=25000:

    credit_score = int(input("enter credit score="))

    if credit_score>=700:

        print("loan approved")

    else:

        print("low credit score")
else:

    print("income not sufficient")