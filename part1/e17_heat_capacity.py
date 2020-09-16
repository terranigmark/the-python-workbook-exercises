"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

q = amout of heat required
C = substance's specific heat
ΔT = t1 - t2 temperature variation
m = substance's mass
"""

def main(c_specific_heat, temp1, temp2, mass):
    kwh_rate = 0.089
    temp_variation = temp2 - temp1
    q_amount_heat = mass * c_specific_heat * temp_variation
    energy_kwh = q_amount_heat / 3_600_000
    energy_cost = energy_kwh * kwh_rate

    return print(f'''
    To bring a mass of {mass} from {temp1} to {temp2} with a specific heat of {c_specific_heat} J/gC...
    It's required a total heat of {q_amount_heat} cal.
    This is equals to {round(energy_kwh, 4)}kWh and around to {round(energy_cost, 4)} USD.
    ''')

if __name__ == "__main__":
    print("Enter the data required to calculate the amount of heat required.")
    c_specific_heat = float(input("Substance's specific heat: "))
    temp1 = float(input("Substance's initial temperature: "))
    temp2 = float(input("Substance's desired temperature to achieve: "))
    mass = float(input("Substance's mass: "))

    main(c_specific_heat, temp1, temp2, mass)