import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

go_next = True
while go_next:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"Sorry, only letters in the alphabet please {error_message}")
    else:
        print(output_list)
        go_next = False

