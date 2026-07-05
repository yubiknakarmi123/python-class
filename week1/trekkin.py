num_trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS fee per person: "))
acap_fee = float(input("Enter ACAP fee per person: "))

per_person_cost = tims_fee + acap_fee
total_cost = per_person_cost * num_trekkers
service_charge = total_cost * 0.05
total_with_service = total_cost + service_charge
average_cost = total_with_service / num_trekkers

print(f"Total cost for group: Rs {total_with_service:.2f}")
print(f"Average cost per person: Rs {average_cost:.2f}")