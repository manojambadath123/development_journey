
p=40000
annual_rate=6
r=annual_rate/(100*12)
print(r)
n=5*12
print(n)
emi_amount=(p*r*(1+r)**n)/((1+r)**n-1)

print("EMI Amount=",emi_amount)

