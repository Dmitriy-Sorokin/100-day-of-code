# numbers = [1, 2, 3]
#
# new_numbers = [n + 1 for n in numbers]
#
# print(new_numbers)
# name = "Angela"
#
# new_list = [letter for letter in name ]
#
# print(new_list)
#
# r_l = [num * 2 for num in range(1, 5)]
# print(r_l)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# apper_name = [name.upper() for name in names if len(name) > 5]
# print(6**2)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
#
#
# #Write your code 👆 above:
# result = [num for num in numbers if num % 2 == 0]
# print(result)
# #
# l_num1 = ["3", "6", "5", "8", "33", '12', '7', "4", "72", "2", "42", "13"]
# l_num2 = ["3", "6", "13", "5", "7", "89", "12", "3", "33", "34", "1", "344", "42"]
#
# result = []
#
# m = [result.append(int(n)) for n in l_num1 if n in l_num2]
#
# print(result)

with open("file1.txt") as file1:
    s1 = file1.readlines()

with open("file2.txt") as file2:
    s2 = file2.readlines()

# Write your code above 👆
result = []

m = [result.append(int(n)) for n in s1 if n in s2]

print(result)


