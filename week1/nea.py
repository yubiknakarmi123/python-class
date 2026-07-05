previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
rate_per_unit = float(input("Enter rate per unit (Rs): "))
service_charge = float(input("Enter fixed service charge (Rs): "))

units_consumed = current_reading - previous_reading
total_bill = (units_consumed * rate_per_unit) + service_charge

print(f"Units consumed: {units_consumed:.2f}")
print(f"Total bill: Rs {total_bill:.2f}")