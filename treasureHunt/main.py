# Treasure Hunt Instructions:
#
# Scenario Setup:
# Imagine a 5x5 grid where a player starts at the top-left corner
# (position [0][0]), and the treasure is at the bottom-right corner ([4][4]).
# Obstacles are placed at specific positions (e.g., [2][1], [3][3]).
# You must write Python code to move the player to the treasure
# using loops while avoiding the obstacles.

#Goal:
# Complete the code by moving the player step-by-step
#using loops (while or for) and conditionals to avoid obstacles.
#

# Starter Code:
# Provide this starter code to help them begin:

# Solution for the Treasure Hunt Exercise
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
    [".", ".", ".", ".", "T"]   # T is the treasure
]

# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

# Start position of the player
player_pos = [0, 0]

# Move the player to the treasure (write your loop here)
while player_pos != [4, 4]:
    # Example: Update player_pos to move right or down
    # Avoid obstacles (e.g., grid[2][1] and grid[3][3])
    pass

print("Treasure found!")