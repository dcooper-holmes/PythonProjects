import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

app_running = True;

def caesar(text, shift, direction):

    end_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:

        if letter in alphabet:
            alphabet_index_shift = alphabet.index(letter)
            new_position = alphabet_index_shift + shift 
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"The {direction}d text is {end_text}")

while app_running == True:
    os.system('cls')
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    caesar(text=text, shift=shift, direction=direction)

    if input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower() == "no":
        app_running = False
        os.system('cls')
        print("CaesarsCipher has now stopped, you may close this window.")
