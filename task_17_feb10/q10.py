
def prime(num):

    is_prime = True

    for i in range(2,num):

        if num%i==0:

            is_prime = False
            return is_prime
        
        else:

            is_prime = True

            return is_prime


result = prime(7)
print(result)
result = prime(8)
print(result)