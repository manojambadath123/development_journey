
data = {
    "apple": 50,
    "banana": 100,
    "cherry": 80,
    "date": 120
}


max_key = max(data, key=data.get)

print(f"The key with the highest value is = {max_key}")

