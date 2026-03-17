

products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]


product_names = [lst[1] for lst in products]

# print(product_names)

high_pr = max([lst[4] for lst in products])

highest_price = [lst[1] for lst in products if lst[4]==high_pr]

# print(highest_price)

electronic_products = [lst[1] for lst in products if lst[3]=="Electronics"]

# print(electronic_products)

products = [lst[1] for lst in products if lst[2]=="Apple"]

# print(products)

# maximum_stock = max([lst[5] for lst in products])

# print(maximum_stock)

# max_stock_name = [lst[1] for lst in products if lst[5]==maximum_stock]

# print(max_stock_name)

categories = [lst[3] for lst in products]

print(categories)
