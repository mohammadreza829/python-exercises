# from random import randint

# # ساخت ماتریس 12x12 با حاشیه صفر
# matrix = [[0] * 12 for _ in range(12)]

# # پر کردن بخش میانی 10x10 با اعداد تصادفی
# for i in range(1, 11):  # از سطر 1 تا 10
#     for j in range(1, 11):  # از ستون 1 تا 10
#         matrix[i][j] = randint(0, 1)

# # چاپ ماتریس
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(matrix[i][j], end="  ")
#     print()

# # گرفتن مختصات موش
# mouse_row = int(input("Enter mouse row (1-10): "))
# mouse_col = int(input("Enter mouse col (1-10): "))

# # گرفتن مختصات پنیر
# cheese_row = int(input("Enter cheese row (1-10): "))
# cheese_col = int(input("Enter cheese col (1-10): "))

# # تعریف جهت‌های حرکت (8 همسایه)
# directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# # تابع جستجو
# def find_path(current_row, current_col, cheese_row, cheese_col):
#     # اگر به پنیر رسیدیم
#     if current_row == cheese_row and current_col == cheese_col:
#         return True

#     # علامت‌گذاری خانه فعلی (برای جلوگیری از حلقه)
#     matrix[current_row][current_col] = 2

#     # بررسی هر 8 همسایه
#     for direction in directions:
#         new_row = current_row + direction[0]
#         new_col = current_col + direction[1]

#         # اگر همسایه معتبر است و راه هست (مقدار 1 دارد)
#         if 1 <= new_row <= 10 and 1 <= new_col <= 10: 
#             if matrix[new_row][new_col] == 1:
#                 if find_path(new_row, new_col, cheese_row, cheese_col):
#                     return True

#     # اگر هیچ مسیری پیدا نشد
#     return False

# # فراخوانی تابع (اسم متغیرها رو درست کردم)
# result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)

# # چاپ نتیجه
# if result:
#     print("مسیر پیدا شد! 🧀")
# else:
#     print("مسیری پیدا نشد! 😞")
    
    
    
#--------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    
from random import randint

# Create 12x12 matrix with zero border
matrix = [[0] * 12 for _ in range(12)]

# Fill the inner 10x10 area with random 0s and 1s
for i in range(1, 11):  # Rows 1 to 10
    for j in range(1, 11):  # Columns 1 to 10
        matrix[i][j] = randint(0, 1)

# Print initial matrix
print("Initial Matrix:")
for i in range(1, 11):  # Print only the inner part
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()

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
                if find_path(new_row, new_col, cheese_row, cheese_col):
                    return True

    # If no path found
    return False


# Call the function
print("\nSearching for path...")
result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)

# Print result
if result:
    print("\nPath found! 🧀")
else:
    print("\nNo path found!")

# Display final matrix
print("\nFinal Matrix (2 = visited cells):")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()
