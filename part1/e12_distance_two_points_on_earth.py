"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers
"""
from math import acos, sin, cos, radians

def main(lat1, long1, lat2, long2):
    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)

    distance = 6371.01 * acos(sin(lat1_rad) * sin(lat2_rad) + cos(lat1_rad) * cos(lat2_rad) * cos(long1_rad - long2_rad))

    return print(f"The distance between point 1 ({lat1}, {long1}) and point 2 ({lat2}, {long2}) is: {round(distance, 2)}km")

if __name__ == "__main__":
    lat1 = float(input("What's the latitude of the first point?: "))
    long1 = float(input("What's the longitude of the first point?: "))
    lat2 = float(input("What's the latitude of the second point?: "))
    long2 = float(input("What's the longitude of the second point?: "))

    main(lat1, long1, lat2, long2)