with open("my_file") as file:
    contents = file.read()
    print(contents)

with open("my_file", mode="a") as file:
    file.write("\nNew text.")

