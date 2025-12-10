# Space Mission Planner

from space_math import calculate_fuel, time_to_destination, gravity_force

# Mission parameters
distance = 225000000  # km
speed = 20000  # km/h
planet_mass = 6.39e23  # kg
spacecraft_mass = 15000  # kg

# Use the imported functions to calculate mission details
fuel_needed = calculate_fuel(distance)
travel_time = time_to_destination(distance, speed)
grav_force = gravity_force(planet_mass, spacecraft_mass, distance)

# Print the mission details
print("Space Mission Details:")
print("----------------------")
print(f"Fuel needed: {fuel_needed:.2f} liters")
print(f"Time to destination: {travel_time:.2f} hours")
print(f"Gravitational force at destination: {grav_force:.2f} N")
