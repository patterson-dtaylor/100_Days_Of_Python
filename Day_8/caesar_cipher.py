cipher_switch = True
print("Welcome to the caesar cipher!")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    cipher_text = ""
    for c in text:
        if c in alphabet:
            if direction == "encode":
                i = alphabet.index(c)
                new_index = i + shift

                if new_index > 25:
                    cipher_text += alphabet[new_index - 26]
                elif new_index <= 25:
                    cipher_text += alphabet[new_index]

            elif direction == "decode":
                i = alphabet.index(c)
                new_index = i - shift

                if new_index < 0:
                    cipher_text += alphabet[new_index + 26]
                elif new_index >= 0:
                    cipher_text += alphabet[new_index]
        else:
            cipher_text += c
    
    print(cipher_text)

while cipher_switch:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction, text=text, shift=shift)
    
    cipher_on_or_off = input("Would you like to encode or decode another message? y/n ")
    if cipher_on_or_off == "n":
        cipher_switch = False
        print("Goodbye!")