class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []   

    def book_seat(self, seat_number, passenger_name):
        for seat, _ in self.booked:
            if seat == seat_number:
                print("Seat already booked")
                return
        self.booked.append((seat_number, passenger_name))

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print("Passenger List:")
        for seat, name in self.booked:
            print(f"Seat {seat}: {name}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),        # duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),     # duplicate
]

for seat, name in bookings:
    bus.book_seat(seat, name)

print(f"\nAvailable Seats: {bus.available_seats()}")
bus.passenger_list()