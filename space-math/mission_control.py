missions = []
mission_details = {}

def add_mission(missions, mission_details, name, details):
    missions.append(name)
    mission_details[name] = details
    print("Mission added successfully!")

def update_mission(mission_details, name, key, value):
    if name in mission_details:
        mission_details[name][key] = value
        print(f"Updated {key} for mission {name}")
    else:
        print(f"Mission {name} not found")

def display_missions(missions, mission_details):
    print("\nAll Missions:")
    for i, mission in enumerate(missions, 1):
        print(f"{i}. {mission}")
        for key, value in mission_details[mission].items():
            print(f"   {key}: {value}")
        print()

def list_astronauts(mission_details):
    all_astronauts = set()
    for mission in mission_details.values():
        crew = mission.get('Crew', '').split(', ')
        all_astronauts.update(crew)
    return all_astronauts

# Main menu loop (provided in the initial script)
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        display_missions(missions, mission_details)

    elif choice == '4':
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
