import time
import random
from contextlib import contextmanager

class WindSimulation:
    def __enter__(self):
        # Simulate starting the wind simulation
        print("Wind simulation started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Simulate stopping the wind simulation
        print("Wind simulation stopped")

    def generate_wind_data(self):
        # Simulate generating random wind direction and speed
        direction = random.randint(0, 360)  # Wind direction in degrees
        speed = random.uniform(0, 30)       # Wind speed in meters per second
        return direction, speed

class Plane:
    def __init__(self, name):
        self.name = name

    def fly_in_wind(self, wind_direction, wind_speed):
        # Simulate the plane adjusting its course based on wind
        print(f"{self.name} flying in wind - Direction: {wind_direction}, Speed: {wind_speed} m/s")

# Example usage
with WindSimulation() as wind_sim:
    # Inside this block, you can get simulated wind data
    for i in range(5):
        wind_direction, wind_speed = wind_sim.generate_wind_data()

        # Create a plane and simulate it flying in the current wind conditions
        plane = Plane(f"Plane {i+1}")
        plane.fly_in_wind(wind_direction, wind_speed)

        time.sleep(1)  # Simulating some time between wind updates

# Outside the 'with' block, the wind simulation is stopped automatically
print("Wind simulation context exited")
