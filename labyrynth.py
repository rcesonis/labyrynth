import random
from colorama import Fore, Style, init

init(autoreset=True)

# Array 20x20
labyrynth = [[random.randint(1, 9) for _ in range(20)] for _ in range(20)]

# Initial coordinates
row, col = 0, 0

# Find highest neigbhour
def find_highest_neighbor(labyrynth, row, column):
    maxValue = 0
    maxRow, maxColumn = row, column

    for rowChange, columnChange in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newRow, newColumn = row + rowChange, column + columnChange
        if 0 <= newRow < 20 and 0 <= newColumn < 20 and labyrynth[newRow][newColumn] > maxValue:
            maxValue = labyrynth[newRow][newColumn]
            maxRow, maxColumn = newRow, newColumn

    return maxRow, maxColumn

# Main
path = []
while True:
    # Find the position of the next highest neibhour
    nextRow, nextColumn = find_highest_neighbor(labyrynth, row, col)

    # Check if all neighbors is zeros
    neighbors = []
    for rowChange, columnChange in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newRow, newCol = nextRow + rowChange, nextColumn + columnChange
        if 0 <= newRow < 20 and 0 <= newCol < 20:
            neighbors.append(labyrynth[newRow][newCol])

    if all(neighbor == 0 for neighbor in neighbors):
        break
    labyrynth[row][col] = 0
    path.append((row, col))
    row, col = nextRow, nextColumn

# Print labyrynth
for r in range(20):
    for c in range(20):
        if (r, c) in path:
            print(Fore.GREEN + str(labyrynth[r][c]), end=" " + Style.RESET_ALL) 
        else:
            print(labyrynth[r][c], end=" ")
    print()
