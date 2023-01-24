alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(direction_cesar, text_cesar, shift_cesar):
    cipher_text = ""
    for letter in text_cesar:
        position = alphabet.index(letter)
        if direction_cesar == "encode":
            new_position = position + shift_cesar
            cipher_text += alphabet[new_position]
        if direction_cesar == "decode":
            new_position = position - shift_cesar
            cipher_text += alphabet[new_position]
    if direction_cesar == "encode":
        print(f"The encoded text is {cipher_text}")
    if direction_cesar == "decode":
        print(f"The decoded text is {cipher_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(direction_cesar=direction, text_cesar=text, shift_cesar=shift)
