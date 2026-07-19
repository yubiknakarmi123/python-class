def ticket_price(seat_type, count):
    if seat_type == "recliner":
        price = 700
    else:  # regular
        price = 400
    return price * count
 
print(ticket_price("regular", 3))
print(ticket_price("recliner", 2))
