

word = "aman##aplan**panamawith2car1bike"
count_alpha=0
count_digit=0
count_special=0

for ch in word:

    if ch.isalpha():

        count_alpha+=1

    elif ch.isdigit():

        count_digit+=1

    elif not ch.isalnum():

        count_special+=1

print(f"count of alphabets={count_alpha}")
print(f"count of digits={count_digit}")
print(f"count of special characters={count_special}")

