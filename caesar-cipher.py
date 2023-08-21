alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#moving the characters in alphabet by the amount user set
def encrypt (p_text, move):
    encrypted_text = ""
    for char in p_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + move) % 26
            encrypted_text += alphabet[new_position]
    return encrypted_text
        
        
  
#checking if we are encrypting or decrypting text
if direction == "encode":
    encrypted_msg = encrypt(text, shift)
    print(encrypted_msg)
elif direction == "decode":
    decrypted_msg = encrypt(text, -shift)
    print(decrypted_msg)