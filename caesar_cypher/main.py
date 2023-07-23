alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo 
print(logo)
def caesar(dir, txt, shft):
        output_text = ""
        if dir == 'decode':
            shft *= -1
        for char in txt:
            if char in alphabet:
                output_text += alphabet[(alphabet.index(char) + shft) % 26]
            else:
                output_text += char
        print(f'The {dir}d text is {output_text}')
       

play = True
while play == True: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))       
    caesar(dir=direction, txt=text, shft=shift)

    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if replay == 'no':
        play = False
        print("goodbye")


#NOTE: previous versions used separate functions for encode and decode
# def encrypt(plain_text, shift_amount):
#     encrypted_text = "" 
#     for char in plain_text:
#         encrypted_text += alphabet[(alphabet.index(char) + shift_amount) % 26]
#         #NOTE: using modulo 26 on shifted text index eliminates 11 lines of code
#         # if shift_amount >= 0:
#         #     char = str(plain_text[_])
#         #     if alphabet.index(char) + shift_amount < 26 or shift_amount == 0:
#         #         encrypted_text += alphabet[alphabet.index(char) + shift_amount]
#         #     elif alphabet.index(char) + shift_amount > 25:
#         #         encrypted_text += alphabet[alphabet.index(char) - (26 - shift_amount)]
#         # else:
#         #     char = str(plain_text[_])
#         #     if alphabet.index(char) + shift_amount > 0:
#         #         encrypted_text += alphabet[alphabet.index(char) + shift_amount]
#         #     elif alphabet.index(char) + shift_amount < 0:
#         #         encrypted_text += alphabet[alphabet.index(char) + (26 + shift_amount)]
#     print(f"The encoded text is {encrypted_text}")
    
# def decrypt(encrypted_text, shift_amount):
#     plain_text = ""
#     for char in encrypted_text:
#         plain_text += alphabet[(alphabet.index(char) - shift_amount) % 26]    
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

