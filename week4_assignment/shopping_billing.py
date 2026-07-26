
def process_order(inventory, cart):
    grand_total = 0 #add through loop of cart
    print("---- Total Bill ----")
 
    for item in cart:
        qty = cart[item]
        if qty <= inventory[item]["stock"]: #check stock 
            price = inventory[item]["price"]
            item_total = price * qty
            grand_total = grand_total + item_total
            inventory[item]["stock"] = inventory[item]["stock"] - qty
            print(item + " x" + str(qty) + " = NPR " + str(item_total))
        else:
            print("Not enough stock  " + item)
 
    print("Grand total: NPR " + str(grand_total))
    print("--------------")
 
    print("Updated inventory:")
    for item in inventory:
        print(item + " -> stock:", inventory[item]["stock"])

inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}
 
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
 
process_order(inventory, cart)
