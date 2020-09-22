"""
In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.
"""

def main(chart, frequency):

    if frequency in chart['frequencies']:
        index = chart['frequencies'].index(frequency)
        return print(f"A frequency of {frequency} Hz is equivalent to {chart['notes'][index]} note")
    elif frequency > 261.63 and frequency < 293.66:
        return print(f"A frequency of {frequency} is between C4 and D4 notes.")
    elif frequency > 293.66 and frequency < 329.63:
        return print(f"A frequency of {frequency} is between D4 and E4 notes.")
    elif frequency > 329.63 and frequency < 349.23:
        return print(f"A frequency of {frequency} is between E4 and F4 notes.")
    elif frequency > 349.23 and frequency < 392.00:
        return print(f"A frequency of {frequency} is between F4 and G4 notes.")
    elif frequency > 392.00 and frequency < 440.00:
        return print(f"A frequency of {frequency} is between G4 and A4 notes.")
    elif frequency > 440.00 and frequency < 493.88:
        return print(f"A frequency of {frequency} is between A4 and B4 notes.")
    else:
        return print("the frequency does not correspond to a known note")

if __name__ == "__main__":
    chart = {
        'notes': ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
        'frequencies': [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
    }

    print("This program reads a frequency and tells you a note that it's close to it")
    frequency = float(input("Enter a frequency: "))

    main(chart, frequency)