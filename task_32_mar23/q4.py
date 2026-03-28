


string = "programming"

v_count=0
c_count=0

vowels="aeiouAEIOU"

for ch in string:

    if ch in vowels:

        v_count+=1

    else:
        
        c_count+=1

print(v_count)
print(c_count)

