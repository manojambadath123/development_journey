

fr = open("file_operations\\orders.txt","r")

# all_orders = []

# for line in fr:

#     all_orders.append(line.rstrip("\n"))

# print(all_orders)



# all_orders = [line.rstrip("\n") for line in fr]

# print(all_orders)



all_orders = [line.rstrip("\n") for line in fr]

print(all_orders)

order_count = {o:all_orders.count(o) for o in all_orders}

print(order_count)
