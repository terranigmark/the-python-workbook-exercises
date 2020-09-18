"""
In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.
"""

def main(seconds, minutes, hours, days):
    days = seconds // SECONDS_PER_DAY
    seconds %= SECONDS_PER_DAY

    hours = seconds // SECONDS_PER_HOUR
    seconds %= SECONDS_PER_HOUR

    minutes = minutes // SECONDS_PER_MINUTE
    seconds %= SECONDS_PER_MINUTE

    return print(f"The equivalent are {days}:{hours}:{minutes}:{seconds}")

if __name__ == "__main__":
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    minutes, hours, days = 0, 0, 0

    print("This program convert an amount of seconds to the format D:HH:MM:SS")
    seconds = int(input("Enter the amount of seconds to convert: "))
    main(seconds, minutes, hours, days)