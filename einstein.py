# Prompt the user for mass in kilograms
mass = int(input("Enter mass (in kilograms): "))

# Explanation: This part of the code uses the 'input()' function to prompt the user to enter a value for mass in kilograms. The user is instructed to input this value, and the entered value is stored in the 'mass' variable.

# Calculate the energy using E=mc^2 (where c = speed of light in m/s)
speed_of_light = 3 * 10**8  # m/s
energy = mass * speed_of_light**2

# Explanation: In this section, the code calculates the energy using the famous equation E=mc^2, where 'E' represents energy, 'm' is the mass, and 'c' is the speed of light. The value of the speed of light is defined as 3 * 10^8 meters per second (m/s). The energy is calculated by squaring the speed of light and multiplying it by the mass, and the result is stored in the 'energy' variable.

# Output the equivalent number of Joules
print(energy)

# Explanation: Finally, the code prints the calculated energy, which represents the equivalent amount of energy in Joules. This is the result of applying the mass-energy equivalence principle, E=mc^2, to the input mass provided by the user.
