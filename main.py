import random # Import random to choose a random event

game_name = "Escaping"  # Name of your game project
print(f"Welcome to {game_name}!") # Greeting with f-string
print("=======================") # TODO, add or remove equal symbol to align the greetings

# Ask for the character's name
name = input("Before we begin, what is your character's name?\n> ")

# Build player dictionary
player = {
    'name': name,
    'health': 100,
    'coin': 0
}

# Print the name using f-string
print(f"Great, {player['name']}! Let's begin the adventure!")

# Build list of events
events = ["find a coin", "meet a monster", "do nothing"]

# Randomly choose one event from the list
event = random.choice(events)
print(f"While exploring, you {event}!")

# Update character stats based on the event
if event == "find a coin":
    player['coin'] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player['health'] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    # "do nothing" event
    pass  # No changes to stats
