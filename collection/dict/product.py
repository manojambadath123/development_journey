

product = {"id":1,"title":"juice","price":15,"avl_qty":25}

print(product)

# print(product["id"])
# print(product["title"])
# print(product["price"])
# print(product["avl_qty"])


product["avl_qty"]+=10

# print(product["avl_qty"])

print(product)


product["code"] = "sku12"

print(product)

# check key exist or not

if "offer" in product:

    print("yes")

else:

    print("no")


