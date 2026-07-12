emergency_vehicle = input("Is there an emergency vehicle? (yes/no): ")
pedestrian_waiting = input("Is a pedestrian waiting? (yes/no): ")
traffic_queue = int(input("How many vehicles are waiting? "))

if emergency_vehicle == "yes":
    print("Green Light: Emergency vehicle gets priority.")
else:
    if pedestrian_waiting == "yes":
        print("Green Light: Pedestrians can cross.")
    else:
        if traffic_queue > 10:
            print("Green Light: Heavy traffic queue.")
        else:
            print("Green Light: Normal traffic flow.")