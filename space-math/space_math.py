# Space Math Module

def calculate_fuel(distance):
    # Calculate fuel needed for the journey
    # Formula: fuel = distance * 500
    return distance * 500

def time_to_destination(distance, speed):
    # Calculate time to reach the destination
    # Formula: time = distance / speed
    return distance / speed

def gravity_force(mass1, mass2, distance):
    # Calculate the gravitational force between two objects
    # Formula: force = (G * mass1 * mass2) / (distance ** 2)
    # Where G is the gravitational constant
    G = 6.67430e-11
    return (G * mass1 * mass2) / (distance ** 2)
