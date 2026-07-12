# Trekking Permit Cost Calculator, Yubik Nakarmi


num_trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS card fee per person "))
acap_fee = float(input("Enter ACAP entry permit fee per person "))

service_charge_percent = 5  

per_person_fee = tims_fee + acap_fee
group_total_before_charge = per_person_fee * num_trekkers
service_charge = group_total_before_charge * (service_charge_percent / 100)
group_total = group_total_before_charge + service_charge
average_cost_per_person = group_total / num_trekkers

print(f"\nTotal permit cost (before service charge): Rs {group_total_before_charge}")
print(f"Agency service charge ({service_charge_percent}%): Rs {service_charge}")
print(f"Total cost for the group: Rs {group_total}")
print(f"Average cost per person: Rs {average_cost_per_person}")