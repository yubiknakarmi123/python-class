inventory = [ #inventry as a list of dictionaries
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]
 
print("--- Inventory Restock Alert ---")
restock_count = 0
for entry in inventory:
    if entry["stock"] < entry["threshold"]:
        print(f"Restock alert: {entry['item']} (stock: {entry['stock']}, threshold: {entry['threshold']})")
        restock_count += 1
print(f"Total items needing restock: {restock_count}")
