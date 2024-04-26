class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make        # Brand of the car, e.g., Toyota
        self.model = model      # Model of the car, e.g., Corolla
        self.color = color      # Color of the car
        self.mileage = mileage  # Mileage of the car

    def drive(self, distance):
        self.mileage += distance
        print(f"Driving {distance} miles. New mileage is {self.mileage} miles.")

    def honk(self):
        print("Beep beep!")

# Creating car instances
my_car = Car("Toyota", "Corolla", "Blue", 50000)
dream_car = Car("Tesla", "Model S", "Red", 5)

# Using car methods
my_car.drive(100)
my_car.honk()

dream_car.drive(200)
dream_car.honk()
