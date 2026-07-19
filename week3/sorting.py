orders = [("O1", 25), ("O2", 10), ("O3", 40), ("O4", 5)]
orders.sort(key=lambda order: order[1])
 
print(orders)