class MetroCard:
    def __init__(self, default_amount=100):
        # Initialize the MetroCard with a default balance
        self.balance = default_amount
        self.stations_traveled = 0

    def top_up(self, amount):
        # Add funds to the MetroCard balance
        self.balance += amount

    def calculate_fare(self):
        # Calculate the fare based on the number of stations traveled
        if self.stations_traveled <= 3:
            return 15
        else:
            fare = 15 + (self.stations_traveled - 3) * 5
            discount_count = self.stations_traveled // 5
            fare -= (discount_count * 5)
            return fare

    def enter_station(self):
        # Check if the balance is sufficient to enter the station
        if self.balance >= 15:
            print("Welcome! You can enter the station.")
        else:
            print("Insufficient balance. Please top up your card.")

    def exit_station(self):
        # Calculate the fare and deduct it from the balance upon exiting the station
        fare = self.calculate_fare()
        if self.balance >= fare:
            self.balance -= fare
            self.stations_traveled += 1
            print(f"You have successfully exited the station. Fare deducted: Rs. {fare}")
        else:
            print("Insufficient balance. Please top up your card.")

# Example usage
card = MetroCard()  # Create a new card with default balance

# Top up the card
card.top_up(200)

# Enter the station
card.enter_station()

# Exit the station
card.exit_station()
