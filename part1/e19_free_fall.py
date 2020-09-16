"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.
"""
from math import sqrt

def main(acceleration, initial_speed, distance):
    final_speed = sqrt((initial_speed**2) + (2 * acceleration * distance))

    return print(f'''
    Taking the following data...
    Initial speed: {initial_speed} m/s
    Acceleration: {acceleration} ms/s2
    Distance: {distance} m

    The final speed is {final_speed} m/s
    ''')

if __name__ == "__main__":
    acceleration = 9.8
    initial_speed = 0
    distance = float(input("Enter the distance traveled in meters of a falling object: "))

    main(acceleration, initial_speed, distance)