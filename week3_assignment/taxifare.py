def taxi_fare(distance, hour):
    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + (distance - 2) * 35
    else:
        fare = 150 + 8 * 35 + (distance - 10) * 28
 
    if hour >= 22 or hour < 5:
        fare *= 1.10
    return fare
 
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]
 
print("--- Taxi Fare Calculator ---")
for trip in trips:
    fare = taxi_fare(trip["distance"], trip["hour"])
    print(f"Distance: {trip['distance']} km, Hour: {trip['hour']} -> Fare: NPR {fare}")