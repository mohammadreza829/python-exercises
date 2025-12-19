students_table = [
    [0, "Ali Rezaei", 1001],
    [1, "Maryam Ahmadi", 1002],
    [2, "Saeid Abbasi", 1003],
    [3, "Negin Kazemi", 1004],
    [4, "Zahra Mohseni", 1005],
    [5, "Amir Mohammadi", 1006],
    [6, "Samira Ghorbani", 1007],
    [7, "Hasan Karimi", 1008],
    [8, "Neda Shahi", 1009],
    [9, "Reza Mahmoudi", 1010]
]

name = input().strip()

found = False
result_index = 0

for idx, student_name, chair in students_table:
    if student_name == name:
        found = True
        result_index = chair
        break

if found:
    print([True, result_index])
else:
    print([False, "Not in this class"])
