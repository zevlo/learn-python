# Prompt user for input
full_name = input("Enter astronaut's full name: ")

# Process the name
uppercase_name = full_name.upper()
underscored_name = uppercase_name.replace(" ", "_")
name_tag = "ASTRONAUT_" + underscored_name

# Print results
print(f"Original name: {full_name}")
print(f"Processed name tag: {name_tag}")
