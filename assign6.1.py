########################################################1
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        if change_speed >= 0:
            self.current_speed = min(self.current_speed + change_speed, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + change_speed, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

# Main program

# Create a new car
car = Car(registration_number="ABC-123", max_speed=142)

# Print initial car properties
print("Initial Car Properties:")
print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km\n")

# Accelerate the car
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

# Print current speed
print(f"Current Speed after acceleration: {car.current_speed} km/h\n")

# Apply emergency brake
car.accelerate(-200)

# Print final speed
print(f"Final Speed after emergency brake: {car.current_speed} km/h\n")

# Drive the car for 1.5 hours
car.drive(1.5)

# Print updated travelled distance
print(f"Travelled Distance after driving: {car.travelled_distance} km\n")
#############################################2
# Drive the car for 1.5 hours
car.drive(1.5)

# Print updated travelled distance
print(f"Travelled Distance after driving: {car.travelled_distance} km\n")



##########################################3

# Car race simulation
car_objects = [Car(registration_number=f"ABC-{i}", max_speed=random.randint(100, 200)) for i in range(1, 11)]

race_distance = 0
hour = 1

print("{:<15} {:<15} {:<15} {:<15}".format("Registration", "Max Speed (km/h)", "Current Speed", "Travelled Distance"))
print("-" * 60)

while race_distance < 10000:
    print(f"\nRace Hour: {hour}")

    for car_obj in car_objects:
        change_speed = random.randint(-10, 15)
        car_obj.accelerate(change_speed)
        car_obj.drive(1)

        print("{:<15} {:<15} {:<15} {:<15}".format(
            car_obj.registration_number,
            car_obj.max_speed,
            car_obj.current_speed,
            car_obj.travelled_distance
        ))

        if car_obj.travelled_distance >= 10000:
            print(f"\nCar {car_obj.registration_number} has finished the race!")
            exit()

    hour += 1

    
###################################4
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        if destination_floor > self.top_floor or destination_floor < self.bottom_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


# Main program
if __name__ == "__main__":
    # Create an elevator
    elevator_h = Elevator(bottom_floor=1, top_floor=10)

    # Move the elevator to floor 5
    elevator_h.go_to_floor(5)

    # Move the elevator back to the bottom floor
    elevator_h.go_to_floor(1)
