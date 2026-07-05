usd_amount = float(input("Enter USD amount sent: "))
exchange_rate = float(input("Enter exchange rate (NPR per USD): "))
fee_percent = float(input("Enter service fee percentage: "))

npr_amount = usd_amount * exchange_rate
fee = npr_amount * (fee_percent / 100)
final_amount = npr_amount - fee

print(f"Converted amount: Rs {npr_amount:.2f}")
print(f"Fee charged: Rs {fee:.2f}")
print(f"Final amount received: Rs {final_amount:.2f}")