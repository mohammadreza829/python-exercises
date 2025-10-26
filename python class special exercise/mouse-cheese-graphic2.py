from random import randint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# ------------------------------
# ایجاد ماتریس با حاشیه صفر
# ------------------------------
matrix = [[0] * 12 for _ in range(12)]

for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = randint(0, 1)

print("Initial Matrix:")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()

# ------------------------------
# ورود اطلاعات موش و پنیر
# ------------------------------
mouse_row = int(input("\nEnter mouse row (1-10): "))
mouse_col = int(input("Enter mouse col (1-10): "))

cheese_row = int(input("Enter cheese row (1-10): "))
cheese_col = int(input("Enter cheese col (1-10): "))

if matrix[mouse_row][mouse_col] != 1:
    print("Error: Mouse is on a wall! (Cell value must be 1)")
    exit()

if matrix[cheese_row][cheese_col] != 1:
    print("Error: Cheese is on a wall! (Cell value must be 1)")
    exit()

# ------------------------------
# جهت‌های حرکت (۸ جهت)
# ------------------------------
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

path = [(mouse_row, mouse_col)]

# ------------------------------
# تابع بازگشتی مسیر‌یابی
# ------------------------------
def find_path(current_row, current_col, cheese_row, cheese_col):
    if current_row == cheese_row and current_col == cheese_col:
        return True

    matrix[current_row][current_col] = 2  # علامت بازدید

    for dr, dc in directions:
        new_row, new_col = current_row + dr, current_col + dc
        if 1 <= new_row <= 10 and 1 <= new_col <= 10:
            if matrix[new_row][new_col] == 1:
                print(f"Moving to: ({new_row}, {new_col})")

                path.append((new_row, new_col))
                if find_path(new_row, new_col, cheese_row, cheese_col):
                    return True
                path.pop()

    return False

# ------------------------------
# اجرای الگوریتم
# ------------------------------
print("\nSearching for path...")
result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)

if result:
    print("\nCheese found!")
else:
    print("\nNo path found!")

print("\nFinal Matrix (2 = visited cells):")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()

# ------------------------------
# بخش گرافیکی حرفه‌ای‌تر
# ------------------------------
try:
    plt.style.use("seaborn-v0_8-whitegrid")

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#f7f9fc")
    ax.set_facecolor("#eaf0f7")

    cmap = ListedColormap(["black", "white", "#6fa8dc"])
    ax.imshow(matrix, cmap=cmap, origin="upper", alpha=0.9)

    # مسیر در صورت وجود
    if result and len(path) > 1:
        path_x = [pos[1] for pos in path]
        path_y = [pos[0] for pos in path]
        ax.plot(path_x, path_y, color="limegreen", linewidth=3,
                marker="o", markersize=6, label="Path")

    # نمایش موش و پنیر
    ax.plot(mouse_col, mouse_row, marker="o", color="dodgerblue",
            markersize=14, label="Mouse", markeredgecolor="white")
    ax.plot(cheese_col, cheese_row, marker="*", color="gold",
            markersize=18, label="Cheese", markeredgecolor="black")

    # گرید زیباتر
    ax.set_xticks(np.arange(12) - 0.5, minor=True)
    ax.set_yticks(np.arange(12) - 0.5, minor=True)
    ax.grid(which="minor", color="gray", linestyle="--", linewidth=0.5)

    ax.tick_params(which="both", bottom=False, left=False,
                   labelbottom=False, labelleft=False)
    ax.legend(loc="upper right")
    ax.set_title("Mouse Path Finder", fontsize=16, fontweight="bold", color="#333333")

    plt.show()

except ImportError:
    print("\nMatplotlib not available for visualization")
