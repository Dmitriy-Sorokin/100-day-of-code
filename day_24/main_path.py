PLACEHOLDER = "[name]"

with open(r"..\day_24\Input\Names\invited_names.txt", mode="r", encoding="utf-8") as name:
    data = name.readlines()

with open(r"..\day_24\Input\Letters\starting_letter.txt", mode="r") as letter:
    n_letter = letter.read()
    for name in data:
        stript_name = name.strip()
        new_letter = n_letter.replace(PLACEHOLDER, stript_name)
        print(new_letter)
        with open(fr".\Output\ReadyToSend\letter_for_{stript_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# for names in data:
#     with open(fr"..\day_24\Output\ReadyToSend\letter_for_{names}.txt", mode="r") as new_letters:
#         pass
#         print(new_letters.read())
#         # x = new_letters.write(n_letter)
#         # print(letter)

# with open(r"..\day_24\Input\Letters\starting_letter.txt", mode="a") as letter:
#     letter.read().replace("[name]", data[0])
#     print(letter)
