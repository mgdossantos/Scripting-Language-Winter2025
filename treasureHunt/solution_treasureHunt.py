# Solution for the Treasure Hunt Exercise

# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")


# Grid setup (5x5 grid)
grid = [
    ["P", ".", ".", ".", "."],  # P is the player
    [".", ".", ".", ".", "."],
    [".", "X", ".", ".", "."],  # X is an obstacle
    [".", ".", ".", "X", "."],
    [".", ".", ".", ".", "T"]  # T is the treasure
]

# Start position of the player
player_pos = [0, 0]

# Display the initial grid
display_grid(grid)

# Move the player to the treasure
while player_pos != [4, 4]:
    row, col = player_pos

    # Try to move right if possible
    if col < 4 and grid[row][col + 1] != "X":
        grid[row][col] = "."
        col += 1
        grid[row][col] = "P"
    # Otherwise, try to move down if possible
    elif row < 4 and grid[row + 1][col] != "X":
        grid[row][col] = "."
        row += 1
        grid[row][col] = "P"

    # Update the player's position
    player_pos = [row, col]

    # Display the grid after each move
    display_grid(grid)

print("Treasure found!")