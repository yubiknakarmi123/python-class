def final_amount(total, is_loyalty_member):
    if total < 1000:
        discount = 0
    elif total < 5000:
        discount = 0.05
    elif total < 15000:
        discount = 0.10
    else:
        discount = 0.20
 
    amount = total * (1 - discount)
    if is_loyalty_member:
        amount *= 0.95
    return amount
 
print("---Online Store Discount System ---")
for total, loyal in [(800, False), (3000, False), (3000, True), (20000, True)]:
    print(f"Total: NPR {total}, Loyalty: {loyal} -> Final: NPR {final_amount(total, loyal):.2f}")
print()