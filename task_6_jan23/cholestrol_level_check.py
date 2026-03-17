
cholestrol = int(input("enter your cholestrol count="))

if cholestrol<200:
    print("desirable")
elif cholestrol>=200 and cholestrol<=239:
    print("borderline high")
elif cholestrol>=240:
    print("high cholestrol")