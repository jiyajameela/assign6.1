####continuaton of the answers in the file two as for some reason , the code didn't work when put together.
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
#there is continuation in the next file as the code didn't work when put together with the other.
