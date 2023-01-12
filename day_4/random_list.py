# Import the random module here
# import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# Write your code below this line 👇
# print(names)
# ln = len(names)

# rd = random.randint(0, ln-1)

# print(names[rd])

# rand_name = random.randrange(len(names))

# print(names[rand_name])
item = 2

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
if item == 2:
    dirty_dozen[1].insert(2, "x")
    dirty_dozen[1].pop(3)
print(dirty_dozen)
# dirty_dozen = [fruits, vegetables]
# dirty_dozen.insert([1][0], "X")
# print(dirty_dozen)
