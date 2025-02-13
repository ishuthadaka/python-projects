import datetime

class RailwayBookingSystem:
    def __init__(self):
        self.available_trains = {  # Sample train data (you can expand this)
            "Train123": {"name": "Express", "seats": 100, "booked": {}},
            "Train456": {"name": "Superfast", "seats": 50, "booked": {}},
            "Train789": {"name": "Mail", "seats": 75, "booked": {}},
        }

    def display_trains(self):
        print("\nAvailable Trains:")
        for train_id, train_info in self.available_trains.items():
            print(f"- {train_id}: {train_info['name']} ({train_info['seats'] - len(train_info['booked'])} seats available)")

    def book_ticket(self):
        self.display_trains()
        train_id = input("Enter the Train ID you want to book: ")

        if train_id not in self.available_trains:
            print("Invalid Train ID.")
            return

        train = self.available_trains[train_id]
        available_seats = train['seats'] - len(train['booked'])

        if available_seats == 0:
            print("Sorry, this train is fully booked.")
            return

        num_passengers = int(input("Enter the number of passengers: "))
        if num_passengers > available_seats:
            print("Not enough seats available.")
            return

        passenger_details = []
        for i in range(num_passengers):
            print(f"\nEnter details for Passenger {i+1}:")
            name = input("Name: ")
            age = int(input("Age: "))
            # Add other details like gender, berth preference, etc. if needed.

            passenger_details.append({"name": name, "age": age})

        booking_date_str = input("Enter booking date (YYYY-MM-DD): ")
        try:
            booking_date = datetime.datetime.strptime(booking_date_str, "%Y-%m-%d").date()  # Date validation
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Generate booking IDs (a simple example; make it more robust in a real app)
        booking_ids = []
        for _ in range(num_passengers):
          booking_id = f"{train_id}-{booking_date.strftime('%Y%m%d')}-{len(train['booked']) + len(booking_ids) + 1}"  # Example booking ID
          booking_ids.append(booking_id)

        for i in range(num_passengers):
            train['booked'][booking_ids[i]] = passenger_details[i] # Store passenger details with booking ID

        print("\nBooking Confirmed!")
        for i in range(num_passengers):
          print(f"Booking ID for {passenger_details[i]['name']}: {booking_ids[i]}")
        print(f"Train: {train['name']}")
        print(f"Date: {booking_date}")
        print(f"Number of Passengers: {num_passengers}")

    def cancel_ticket(self):
        train_id = input("Enter the Train ID: ")
        if train_id not in self.available_trains:
            print("Invalid Train ID.")
            return

        booking_id = input("Enter the Booking ID to cancel: ")
        train = self.available_trains[train_id]

        if booking_id in train['booked']:
            del train['booked'][booking_id]
            print("Ticket cancelled successfully.")
        else:
            print("Invalid Booking ID.")

    def run(self):
        while True:
            print("\nRailway Booking System")
            print("1. Book Ticket")
            print("2. Cancel Ticket")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.book_ticket()
            elif choice == '2':
                self.cancel_ticket()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    system = RailwayBookingSystem()
    system.run()