#calculating remmitance, Yubik Nakarmi
def remittance_calculator():
    usd_amount = float(input("Enter USD amount sent: "))
    exchange_rate = float(input("Enter exchange rate (NPR per USD): "))
    fee_percent = float(input("Enter service fee percentage: "))

    npr_amount = usd_amount * exchange_rate
    fee = npr_amount * (fee_percent / 100)
    final_amount = npr_amount - fee
    return npr_amount, fee, final_amount

npr_amount, fee, final_amount = remittance_calculator()

print(f"Converted amount: Rs {npr_amount}")
print(f"Fee charged: Rs {fee}")
print(f"Final amount received: Rs {final_amount}")