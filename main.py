import random # Import random to choose a random event

# Global variables
player = {
    'name': "Tester", # Use string literal instead of input
    'health': 100,
    'coin': 0,
    'x': 0,
    'y': 0
}
map_size = 9
events = ["find a coin", "meet a monster", "do nothing"]

# Function to check an event
def check_event():
    global player, events
    event = random.choice(events)
    if event == "find a coin":
        player['coin'] += 1
    elif event == "meet a monster":
        player['health'] -=10
    else:
        pass # "do nothing"

# Function to draw the map and UI
def draw_ui(x, y):
    print("=" * (map_size * 2 + 7))  # top border
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end=" ")  # Player position
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end=" ")  # Gate position
            else:
                print(".", end=" ")
        print()  # Newline for next row
    print("=" * (map_size * 2 + 7))  # bottom border
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coin: {player['coin']}")
    print("=" * (map_size * 2 + 7))

# Function to move the player
def move(direction):
    if direction == 'w' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] += 1
    elif direction == 'a' and player['x'] > 0:
        player['x'] -= 1
    elif direction =='d' and player['x'] < map_size - 1:
        player['x'] += 1
    # Invalid moves are ignored to pass the unit tests

# Main game loop
def main():
    draw_ui(player['x'], player['y'])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != 'q':
        move(direction)

        # Check if player reached the gate
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reached the gate for next level.")
            break

        check_event()
        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q): ")

# Run the game
if __name__ == '__main__':
    main()
    