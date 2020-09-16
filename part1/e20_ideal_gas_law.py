"""
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 mol K J , and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.
"""

def main(gas_constant, pressure, volume, temperature):
    kelvin_temp = temperature + 273.15
    pressure_times_volume = pressure * volume
    gas_constant_times_temp = gas_constant * kelvin_temp
    result = pressure_times_volume / gas_constant_times_temp

    return print(f"The amount of substance is: {round(result, 4)} moles")

if __name__ == "__main__":
    print("This prorgam will compute the amount of gas in moles according to your inputs")
    gas_constant = 8.314
    pressure = float(input("Enter the presure of the container in Pascals: "))
    volume = float(input("Enter the volume of the gas container in liters: "))
    temperature = float(input("Enter the temperature in Celsius: "))

    main(gas_constant, pressure, volume, temperature)