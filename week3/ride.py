def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type == "bike":
        rate_per_km = 25
    elif vehicle_type == "car":
        rate_per_km = 50
    else:
        rate_per_km = 35  # default
 
    base_fare = 50
    fare = (base_fare + distance_km * rate_per_km) * surge
    return fare
 
print(estimate_fare(5, "bike"))
print(estimate_fare(5, "car", surge=1.5))
