from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Create 12x12 matrix with zero border
matrix = [[0] * 12 for _ in range(12)]

# Fill the inner 10x10 area with random 0s and 1s
for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = randint(0, 1)

# Get mouse coordinates
mouse_row = int(input("\nEnter mouse row (1-10): "))
mouse_col = int(input("Enter mouse col (1-10): "))

# Get cheese coordinates
cheese_row = int(input("Enter cheese row (1-10): "))
cheese_col = int(input("Enter cheese col (1-10): "))

# Check start and end points
if matrix[mouse_row][mouse_col] != 1:
    print("Error: Mouse is on a wall! (Cell value must be 1)")
    exit()

if matrix[cheese_row][cheese_col] != 1:
    print("Error: Cheese is on a wall! (Cell value must be 1)")
    exit()

# Define movement directions (8 neighbors)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Lists to store the path for visualization
path_rows = [mouse_row]
path_cols = [mouse_col]


# Search function
def find_path(current_row, current_col, cheese_row, cheese_col):
    # If we reached the cheese
    if current_row == cheese_row and current_col == cheese_col:
        return True

    # Mark current cell (to prevent loops)
    matrix[current_row][current_col] = 2

    # Check all 8 neighbors
    for direction in directions:
        new_row = current_row + direction[0]
        new_col = current_col + direction[1]

        # If neighbor is valid and is a path (value 1)
        if 1 <= new_row <= 10 and 1 <= new_col <= 10:
            if matrix[new_row][new_col] == 1:
                print(f"Moving to: ({new_row}, {new_col})")

                # Store the path for visualization
                path_rows.append(new_row)
                path_cols.append(new_col)

                if find_path(new_row, new_col, cheese_row, cheese_col):
                    return True

                # If this path didn't lead to cheese, backtrack
                path_rows.pop()
                path_cols.pop()

    # If no path found
    return False


# Call the function
print("\nSearching for path...")
result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)

# Print result
if result:
    print("\nCheese found!")
else:
    print("\nNo path found!")

# Visualization
fig, ax = plt.subplots(figsize=(8, 8))

# Create a colormap for the matrix
cmap = plt.cm.colors.ListedColormap(["black", "white", "lightblue"])
bounds = [0, 1, 2, 3]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

# Display the matrix
ax.imshow(matrix, cmap=cmap, norm=norm, origin="upper")

# Draw grid
ax.grid(which="major", axis="both", linestyle="-", color="k", linewidth=2)
ax.set_xticks(np.arange(-0.5, 12, 1))
ax.set_yticks(np.arange(-0.5, 12, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Plot the path
ax.plot(np.array(path_cols) - 0.5, np.array(path_rows) - 0.5, "r-", linewidth=3)
ax.plot(np.array(path_cols) - 0.5, np.array(path_rows) - 0.5, "ro", markersize=8)

# Mark start (mouse) and end (cheese)
ax.text(mouse_col - 1, mouse_row - 1, "🐭", fontsize=20, ha="center", va="center")
ax.text(cheese_col - 1, cheese_row - 1, "🧀", fontsize=20, ha="center", va="center")

# Set title
ax.set_title("Mouse Finding Cheese Path")

plt.show()
