"""
The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:
Magnitude Descriptor
Less than 2.0 Micro
2.0 to less than 3.0 Very minor
3.0 to less than 4.0 Minor
4.0 to less than 5.0 Light
5.0 to less than 6.0 Moderate
6.0 to less than 7.0 Strong
7.0 to less than 8.0 Major
8.0 to less than 10.0 Great
10.0 or more Meteoric
Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
"""
import math

def main(scale, richter_scale):

    for i in range(len(richter_scale['magnitude'])):
        if scale >= richter_scale['magnitude'][i][0] and scale <= richter_scale['magnitude'][i][1]:
            return print(f"A magnitude of {scale} is a {richter_scale['descriptor'][i]} earthquake.")
        elif scale > 10:
            return print("Now that's a meteoric earthquake!")

if __name__ == "__main__":
    richter_scale = {
        'magnitude': [[0,1.9], [2, 2.9], [3, 3.9], [4, 4.9], [5, 5.9], [6, 6.9], [7, 7.9], [8, 9.9]],
        'descriptor': ['Micro', 'Very minor', 'Minor', 'Light', 'Moderate', 'Strong', 'Major', 'Great', 'Meteoric']
    }

    print("This program tells you the descriptor of a Richter scale magnitude")
    scale = float(input("Enter a magnitude from 0 to 10: "))

    main(scale, richter_scale)