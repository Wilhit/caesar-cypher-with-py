#caesar Cipher
from cipher_art import logo




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(start_text, key, c_direction):
    if c_direction == "decode" or c_direction == "encode": 
        end_text = ""
        if c_direction == "decode":
            key *= -1

        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + key
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {c_direction}d text is {end_text}")
    else:
        print("Wrong Direction Try 'encode'to encrypt, and 'decode' to decrypt")
        print()



should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25

    caesar(start_text = text, key = shift, c_direction = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        input("Good Bye!!!")
