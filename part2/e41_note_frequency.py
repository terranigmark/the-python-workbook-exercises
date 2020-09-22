"""
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
Note Frequency (Hz)
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88
Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement.
"""

def main(chart, note):
    index = 0
    note_char = note[0]
    note_scale = int(note[1])
    note_in_chart = chart['notes'][index][0]
    scale_in_chart = int(chart['notes'][index][1])
    frequency = chart['frequencies'][index]

    if note in chart['notes']:
        index = chart['notes'].index(note)
        print(f"The frequency of the note {note} is {frequency}")
    else:
        for index in range(7):
            if note_char in note_in_chart:
                frequency =  frequency / 2**(4 - note_scale)

        return print(f"The frequency of {note} is {frequency}")


if __name__ == "__main__":
    chart = {
        'notes': ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'],
        'frequencies': [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
    }
    print("This program reads a note and tells you it's frequency in Hz.")
    note = str(input("Enter a note to display it's frequency: "))

    main(chart, note)