# 🚨 Don't change the code below 👇
#           "1"  "2"  "3"
row1 = ["1""⬜", "⬜", "⬜"]
row2 = ["2""⬜", "⬜", "⬜"]
row3 = ["3""⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input(
    "Where do you want to put the treasure? ")  # position = "32" | 2 это номер списка | 3 индекс элемента в списке
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
hor = int(position[0])
ver = int(position[1])

selected_row = map[ver - 1]  # Выбираем список куда быдем ложить "X"
# print(selected_row)
selected_row[hor - 1] = "X"

# pas = int(position)
#
# if pas == 11:
#     map[0].insert(0, 'X')
#     map[0].pop(1)
# if pas == 12:
#     map[1].insert(0, 'X')
#     map[1].pop(1)
# if pas == 13:
#     map[2].insert(0, 'X')
#     map[2].pop(1)
# if pas == 21:
#     map[0].insert(1, 'X')
#     map[0].pop(2)
# if pas == 22:
#     map[1].insert(1, 'X')
#     map[1].pop(2)
# if pas == 23:
#     map[2].insert(1, 'X')
#     map[2].pop(2)
# if pas == 31:
#     map[0].insert(2, 'X')
#     map[0].pop(3)
# if pas == 32:
#     map[1].insert(2, 'X')
#     map[1].pop(3)
# if pas == 33:
#     map[2].insert(2, 'X')
#     map[2].pop(3)
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
