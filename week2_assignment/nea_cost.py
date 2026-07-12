#NEA cost calculator, YUBIK NAKARMI
def nea_cost_calculator():

    previous_reading = float(input("Enter previous meter reading (kWh): "))
    current_reading = float(input("Enter current meter reading (kWh): "))
    rate_per_unit = float(input("Enter rate per unit (Rs/kWh): "))
    service_charge = float(input("Enter fixed monthly service/meter charge (Rs): "))

    units_consumed = current_reading - previous_reading
    energy_cost = units_consumed * rate_per_unit
    total_bill = energy_cost + service_charge

    return units_consumed, energy_cost, total_bill, service_charge

units_consumed, energy_cost, total_bill, service_charge = nea_cost_calculator()

print(f"\nUnits consumed: {units_consumed} kWh")
print(f"Energy cost: Rs {energy_cost}")
print(f"Service charge: Rs {service_charge}")
print(f"Estimated total bill: Rs {total_bill}")