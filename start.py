import random
import time
import os

width = 52
height = 25

# Create a 2D list of cells
grid = [[random.randint(0,1) for x in range(width)] for y in range(height)]

num_living_cells = sum([sum(row) for row in grid])

# Keep track of the number of iterations where the number of living cells stays the same
consistent_living_cells = 0

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the current state of grid
    for row in grid:
        print(" ".join(["#" if cell else "." for cell in row]))
    print("\n")

    # Get the new state of the grid
    new_grid = [[0 for x in range(width)] for y in range(height)]

    for y in range(height):
        for x in range(width):
            num_neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if x+dx == 0 or x+dx >= width:
                        continue
                    if y+dy < 0 or y+dy >= height:
                        continue
                    if grid[y+dy][x+dx] == 1:
                        num_neighbors += 1
            if grid[y][x] == 1 and num_neighbors in [2,3]:
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and num_neighbors == 3:
                new_grid[y][x] = 1

    grid = new_grid

    # Check if the number of living cells has remained the same
    if sum([sum(row) for row in grid]) == num_living_cells:
        consistent_living_cells += 1
        if consistent_living_cells >= 100:
            grid = [[random.randint(0,1) for x in range(width)] for y in range(height)]
            consistent_living_cells = 0
    else:
        num_living_cells = sum([sum(row) for row in grid])
        consistent_living_cells = 0

    time.sleep(0.5)