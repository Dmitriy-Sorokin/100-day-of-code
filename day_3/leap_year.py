a = 1989

if a % 4 == 0:
    if a % 100 != 0:
        print("leap true")
    elif a % 400 == 0:
        print("leap true")
    else:
        print("Not leap year")
else:
    print("Not leap year")
