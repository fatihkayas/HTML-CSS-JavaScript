# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(3, 4)
# Define a class named Flight
class Flight():
    # Define the constructor method that takes a capacity parameter
    def __init__(self, capacity):
        # Set the capacity attribute of the Flight object to the provided capacity
        self.capacity = capacity
        # Create an empty list to store the passengers
        self.passengers = []

    # Define a method named add_passenger that takes a name parameter
    def add_passenger(self, name):
        # Check if there are open seats on the flight
        if not self.open_seats():
            # If there are no open seats, return False
            return False
        # If there are open seats, add the passenger to the list
        self.passengers.append(name)
        # Return True to indicate that the passenger was added successfully
        return True

    # Define a method named open_seats
    def open_seats(self):
        # Calculate the number of open seats by subtracting the number of passengers from the capacity
        return self.capacity - len(self.passengers)

# Create an instance of the Flight class with a capacity of 3
flight = Flight(3)

# Create a list of people
people = ["Alice", "Bob", "Charlie", "David"]

# Iterate over each person in the list
for person in people:
    # Try to add the person to the flight
    if flight.add_passenger(person):
        # If the person was added successfully, print a success message
        print(f"Added {person} to flight successfully.")
    else:
        # If there are no available seats, print a message indicating that
        print(f"No available seats for {person}.")
        
            
