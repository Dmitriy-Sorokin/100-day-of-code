################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

def en():
    return enemies + 1

print(en())
increase_enemies()
print(f"enemies outside function: {enemies}")