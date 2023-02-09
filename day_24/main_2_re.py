REPLACE_WORD = "[name]"

with open(r".\Input\Names\invited_names.txt") as names:
    inp_names = names.readlines()


with open(r".\Input\Letters\starting_letter.txt") as letter:
    text_letter = letter.read()

for name in inp_names:
    name_strip = name.strip()
    final_letter = text_letter.replace(REPLACE_WORD, name_strip)
    with open(fr'.\Output\ReadyToSend\letter_for_{name_strip}.txt', mode="w") as complete:
        complete.write(final_letter)
