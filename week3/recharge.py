def recharge_cost(gb, validity_days=30):
    if gb <= 1:
        price = 49
    elif gb <= 5:
        price = 199
    elif gb <= 10:
        price = 349
    else:
        price = 599
    return price
 
print(recharge_cost(2))
print(recharge_cost(10, validity_days=15))