"""
The following table lists the sound level in decibels for several common noises.
Noise Decibel level (dB)
Jackhammer 130
Gas lawnmower 106
Alarm clock 70
Quiet room 40
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

def main(sound_level, sounds):
    if sound_level < 40:
        return print("That's quieter than a quiet room itself...")
    elif sound_level > 130:
        return print("That's louder than a jackhammer!")
    elif sound_level in sounds.keys():
        return print(f"That's a loud as a {sounds.get(sound_level)}")
    elif sound_level > 40 and sound_level < 70:
        return print("That's louder than a quiet room but not as much as an alarm clock")
    elif sound_level > 70 and sound_level < 106:
        return print("That's louder than a alarm clock but not as much as a gas lawnmower")
    elif sound_level > 106 and sound_level < 130:
        return print("That's louder than a gas lawnmower but not as much as a jackhammer")

if __name__ == "__main__":
    sounds = {
        130: 'jackhammer',
        106: 'gas lawnmower',
        70: 'alarm clock',
        40: 'quiet room',
    }

    print("This program read a sound level in dB and tells you a similar noise")
    sound_level = int(input("Enter a sound level in dB to compare: "))

    main(sound_level, sounds)